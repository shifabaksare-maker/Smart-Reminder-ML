"""
SMART REMINDER – Machine Learning Based Reminder System
Author: Shifa Baksare (AI & Data Science, 3rd Year)

File: train_model.py
Description: Trains and evaluates ML models (Random Forest, Decision Tree, Logistic Regression)
             for predicting reminder urgency and saves the trained model and encoder.
"""

import os
import sys
import random
import joblib
import numpy as np
import pandas as pd

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score


# Base directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, 'dataset')
MODEL_DIR = os.path.join(BASE_DIR, 'model')
SCREENSHOTS_DIR = os.path.join(BASE_DIR, 'screenshots')
CSV_PATH = os.path.join(DATASET_DIR, 'reminders.csv')
MODEL_PATH = os.path.join(MODEL_DIR, 'reminder_model.pkl')
ENCODER_PATH = os.path.join(MODEL_DIR, 'reminder_encoder.pkl')

os.makedirs(DATASET_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)


def generate_synthetic_dataset(filepath=CSV_PATH, num_samples=1000):
    """Generates a realistic synthetic dataset if not already present."""
    print("[*] Generating realistic reminder dataset...")
    random.seed(42)
    np.random.seed(42)

    tasks_by_category = {
        'Academic': [
            'Submit ML Lab Assignment', 'Prepare for Viva Exam', 'Complete Mini Project Documentation',
            'Study for AI Midterms', 'Submit Research Paper Draft', 'Attend Guest Lecture on Deep Learning',
            'Solve Data Science Problem Set', 'Submit Seminar Abstract', 'Revise Machine Learning Notes',
            'Group Project Discussion', 'Prepare Presentation Slides', 'Submit Final Semester Thesis'
        ],
        'Work': [
            'Client Sprint Review Meeting', 'Submit Weekly Progress Report', 'Bug Triage and Code Review',
            'Deploy Application to Production', 'Team Standup Sync', 'Prepare Product Pitch Deck',
            'Respond to High Priority Client Emails', 'Update Jira Sprint Backlog', 'System Architecture Review',
            'Database Migration Check', 'Security Audit Review', 'Vendor Contract Follow-up'
        ],
        'Health': [
            'Take Prescribed Morning Medication', 'Doctor Consultation Appointment', 'Evening Gym Cardio Workout',
            'Refill Prescription at Pharmacy', 'Drink 2 Liters Water Goal', 'Annual Dental Checkup',
            'Book Blood Test Diagnostics', 'Physiotherapy Session', 'Take Multivitamins & Supplements',
            'Track Daily Calorie Intake', 'Eye Specialist Appointment', 'Morning Yoga and Meditation'
        ],
        'Financial': [
            'Pay Electricity & Utility Bill', 'Credit Card Due Payment', 'File Income Tax Return',
            'Pay Monthly Apartment Rent', 'Review Monthly Bank Statement', 'Transfer Mutual Fund SIP',
            'Pay Wi-Fi Broadband Bill', 'Renew Vehicle Insurance Policy', 'Submit Tuition Fees Payment',
            'Audit Monthly Expense Budget', 'Recharge Mobile Prepaid Plan', 'Pay Health Insurance Premium'
        ],
        'Personal': [
            'Buy Weekly Groceries and Essentials', 'Laundry and Dry Cleaning Pickup', 'Car Servicing and Oil Change',
            'Clean and Organize Work Desk', 'Book Train / Flight Tickets', 'Water Indoor Plants',
            'Read 30 Pages of Book', 'Backup Laptop Hard Drive', 'Renew Passport Documentation',
            'Home Appliance Maintenance', 'Cook Meal Prep for Tomorrow', 'Organize Digital Files & Photos'
        ],
        'Social': [
            'Call Parents and Family', 'Attend Friend\'s Birthday Dinner', 'RSVP for Alumni Reunion',
            'Send Wedding Anniversary Wishes', 'Mentor Junior AI Students', 'Community Volunteer Event',
            'Organize Weekend Get-together', 'Send Festival Greeting Messages', 'Participate in College Tech Fest',
            'Visit Grandparents at Weekend', 'Connect with Mentors on LinkedIn', 'Attend Department Farewell'
        ]
    }

    categories = list(tasks_by_category.keys())
    time_slots = ['Morning', 'Afternoon', 'Evening', 'Night']
    complexities = ['Low', 'Medium', 'High']

    data = []
    for i in range(num_samples):
        cat = random.choice(categories)
        task_name = random.choice(tasks_by_category[cat])
        days_due = int(np.random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14], 
                                      p=[0.10, 0.12, 0.12, 0.10, 0.10, 0.08, 0.08, 0.08, 0.06, 0.06, 0.05, 0.05]))
        
        if cat in ['Academic', 'Financial']:
            importance = int(np.random.choice([2, 3, 4, 5], p=[0.15, 0.25, 0.35, 0.25]))
        elif cat in ['Health', 'Work']:
            importance = int(np.random.choice([2, 3, 4, 5], p=[0.15, 0.25, 0.30, 0.30]))
        else:
            importance = int(np.random.choice([1, 2, 3, 4], p=[0.35, 0.30, 0.25, 0.10]))
            
        est_hours = round(float(np.random.choice([0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0], 
                                                p=[0.15, 0.20, 0.25, 0.15, 0.10, 0.06, 0.04, 0.03, 0.02])), 2)
        complexity = random.choice(complexities)
        time_slot = random.choice(time_slots)
        past_completion = round(float(np.random.uniform(0.45, 0.98)), 2)
        
        # Composite score
        due_factor = (14 - days_due) / 14.0 * 42.0
        imp_factor = (importance / 5.0) * 38.0
        time_factor = (est_hours / 6.0) * 10.0
        comp_val = 10.0 if complexity == 'High' else (6.0 if complexity == 'Medium' else 2.0)
        
        raw_score = due_factor + imp_factor + time_factor + comp_val
        noise = np.random.normal(0, 3.5)
        final_score = raw_score + noise
        
        if final_score >= 68.0:
            urgency = 'High'
        elif final_score >= 46.0:
            urgency = 'Medium'
        else:
            urgency = 'Low'
            
        data.append({
            'Task_ID': f'REM_{i+1:04d}',
            'Task_Name': task_name,
            'Category': cat,
            'Days_Until_Due': days_due,
            'Estimated_Hours': est_hours,
            'Importance_Rating': importance,
            'Task_Complexity': complexity,
            'Time_Slot': time_slot,
            'Past_Completion_Rate': past_completion,
            'Reminder_Urgency': urgency
        })

    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)
    print(f"[OK] Saved {len(df)} records to {filepath}")
    return df


def train_and_evaluate():
    """Loads dataset, trains models, evaluates metrics, and exports artifacts."""
    print("=" * 65)
    print("  SMART REMINDER SYSTEM - MODEL TRAINING PIPELINE")
    print("  Student: Shifa Baksare (AI & DS - 3rd Year)")
    print("=" * 65)

    if not os.path.exists(CSV_PATH):
        df = generate_synthetic_dataset(CSV_PATH)
    else:
        df = pd.read_csv(CSV_PATH)
        print(f"[OK] Loaded existing dataset from {CSV_PATH} ({len(df)} records)")

    print("\n--- DATASET OVERVIEW ---")
    print(df.info())
    print("\n--- CLASS DISTRIBUTION (TARGET: Reminder_Urgency) ---")
    print(df['Reminder_Urgency'].value_counts())

    # Features and Target
    feature_cols = [
        'Category', 'Days_Until_Due', 'Estimated_Hours', 
        'Importance_Rating', 'Task_Complexity', 'Time_Slot', 'Past_Completion_Rate'
    ]
    target_col = 'Reminder_Urgency'

    X = df[feature_cols]
    y = df[target_col]

    cat_cols = ['Category', 'Task_Complexity', 'Time_Slot']
    num_cols = ['Days_Until_Due', 'Estimated_Hours', 'Importance_Rating', 'Past_Completion_Rate']

    # Preprocessing Pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), num_cols),
            ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_cols)
        ]
    )

    # Stratified Train-Test Split (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"\n[OK] Train Set: {len(X_train)} samples | Test Set: {len(X_test)} samples")

    # Fit preprocessor on training data
    X_train_proc = preprocessor.fit_transform(X_train)
    X_test_proc = preprocessor.transform(X_test)

    # Models Comparison
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
        'Decision Tree': DecisionTreeClassifier(max_depth=6, random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42)
    }

    results = {}
    print("\n--- MODEL PERFORMANCE COMPARISON ---")
    for name, clf in models.items():
        clf.fit(X_train_proc, y_train)
        preds = clf.predict(X_test_proc)
        acc = accuracy_score(y_test, preds)
        f1 = f1_score(y_test, preds, average='weighted')
        results[name] = {'Accuracy': acc, 'F1-Score': f1, 'Model': clf}
        print(f"  * {name:<20}: Accuracy = {acc * 100:.2f}% | Weighted F1 = {f1 * 100:.2f}%")

    # Selected Model: Random Forest
    selected_name = 'Random Forest'
    best_clf = results[selected_name]['Model']
    y_pred = best_clf.predict(X_test_proc)
    test_acc = accuracy_score(y_test, y_pred)

    print(f"\n[OK] Selected Primary Model: {selected_name} ({test_acc * 100:.2f}% Test Accuracy)")
    print("\n--- DETAILED CLASSIFICATION REPORT ---")
    print(classification_report(y_test, y_pred, digits=4))

    # Confusion Matrix
    labels = ['High', 'Medium', 'Low']
    cm = confusion_matrix(y_test, y_pred, labels=labels)

    # Save artifacts
    print("\n--- SAVING MODEL & ENCODER ARTIFACTS ---")
    joblib.dump(best_clf, MODEL_PATH)
    print(f"[OK] Model saved to: {MODEL_PATH}")

    # Extract feature names after One-Hot Encoding
    ohe_features = preprocessor.named_transformers_['cat'].get_feature_names_out(cat_cols)
    all_feature_names = num_cols + list(ohe_features)

    encoder_artifact = {
        'preprocessor': preprocessor,
        'cat_cols': cat_cols,
        'num_cols': num_cols,
        'feature_cols': feature_cols,
        'all_feature_names': all_feature_names,
        'classes': best_clf.classes_
    }
    joblib.dump(encoder_artifact, ENCODER_PATH)
    print(f"[OK] Encoder & Preprocessor saved to: {ENCODER_PATH}")

    # Generate visual evaluation plots for PPT & Report
    generate_evaluation_charts(results, cm, labels, best_clf, all_feature_names)

    print("\n" + "=" * 65)
    print("  TRAINING PIPELINE COMPLETE & READY FOR INFERENCE!")
    print("=" * 65)


def generate_evaluation_charts(results, cm, labels, rf_model, feature_names):
    """Generates visualization charts for the presentation and project report."""
    sns.set_theme(style="whitegrid")

    # 1. Confusion Matrix Plot
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=labels, yticklabels=labels, cbar=False,
                annot_kws={"size": 14, "weight": "bold"})
    plt.title('Random Forest - Confusion Matrix', fontsize=13, weight='bold', pad=12)
    plt.xlabel('Predicted Urgency', fontsize=11, labelpad=8)
    plt.ylabel('Actual Urgency', fontsize=11, labelpad=8)
    plt.tight_layout()
    cm_path = os.path.join(SCREENSHOTS_DIR, 'confusion_matrix.png')
    plt.savefig(cm_path, dpi=300)
    plt.close()
    print(f"[OK] Saved confusion matrix chart to: {cm_path}")

    # 2. Feature Importance Plot
    importances = rf_model.feature_importances_
    sorted_idx = np.argsort(importances)[::-1][:10]  # Top 10 features
    top_features = [feature_names[i] for i in sorted_idx]
    top_scores = importances[sorted_idx]

    plt.figure(figsize=(7, 5))
    palette = sns.color_palette("viridis", len(top_features))
    sns.barplot(x=top_scores, y=top_features, palette=palette)
    plt.title('Top 10 Feature Importances (Random Forest)', fontsize=13, weight='bold', pad=12)
    plt.xlabel('Relative Importance Score', fontsize=11, labelpad=8)
    plt.tight_layout()
    fi_path = os.path.join(SCREENSHOTS_DIR, 'feature_importance.png')
    plt.savefig(fi_path, dpi=300)
    plt.close()
    print(f"[OK] Saved feature importance chart to: {fi_path}")

    # 3. Model Accuracy Comparison Plot
    model_names = list(results.keys())
    accuracies = [results[m]['Accuracy'] * 100 for m in model_names]

    plt.figure(figsize=(6, 4.5))
    bars = plt.bar(model_names, accuracies, color=['#4F46E5', '#06B6D4', '#10B981'], width=0.55)
    plt.title('Model Accuracy Comparison', fontsize=13, weight='bold', pad=12)
    plt.ylabel('Test Accuracy (%)', fontsize=11, labelpad=8)
    plt.ylim(70, 100)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.8, f'{yval:.2f}%', ha='center', va='bottom', weight='bold')
    plt.tight_layout()
    comp_path = os.path.join(SCREENSHOTS_DIR, 'model_comparison.png')
    plt.savefig(comp_path, dpi=300)
    plt.close()
    print(f"[OK] Saved model comparison chart to: {comp_path}")


if __name__ == '__main__':
    train_and_evaluate()
