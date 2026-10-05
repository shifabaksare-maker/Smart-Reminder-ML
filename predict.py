"""
SMART REMINDER – Machine Learning Based Reminder System
Author: Shifa Baksare (AI & Data Science, 3rd Year)

File: predict.py
Description: Standalone inference module for predicting reminder urgency and recommended
             actions given reminder task attributes.
"""

import os
import sys
import joblib
import pandas as pd

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'reminder_model.pkl')
ENCODER_PATH = os.path.join(BASE_DIR, 'model', 'reminder_encoder.pkl')

_model = None
_encoder_dict = None


def load_artifacts():
    """Loads the serialized model and preprocessor artifacts."""
    global _model, _encoder_dict
    if _model is None or _encoder_dict is None:
        if not os.path.exists(MODEL_PATH) or not os.path.exists(ENCODER_PATH):
            raise FileNotFoundError(
                f"Model or encoder not found. Please run 'train_model.py' first.\n"
                f"Expected:\n  - {MODEL_PATH}\n  - {ENCODER_PATH}"
            )
        _model = joblib.load(MODEL_PATH)
        _encoder_dict = joblib.load(ENCODER_PATH)
    return _model, _encoder_dict


def predict_reminder(task_name="Submit ML Project",
                     category="Academic",
                     days_until_due=1,
                     estimated_hours=3.0,
                     importance_rating=5,
                     task_complexity="High",
                     time_slot="Morning",
                     past_completion_rate=0.85):
    """
    Predicts the urgency level and generates actionable smart reminder recommendations.
    
    Returns a dictionary containing:
      - task_name
      - category
      - days_until_due
      - predicted_urgency: 'High', 'Medium', or 'Low'
      - confidence: float percentage (e.g. 92.5)
      - probabilities: dict of class -> percentage
      - alert_mode: recommended alert type
      - frequency: recommended notification frequency
      - explanation: student/viva-friendly explanation
      - badge_color: UI styling badge class
    """
    model, encoder_data = load_artifacts()
    preprocessor = encoder_data['preprocessor']

    input_df = pd.DataFrame([{
        'Category': str(category),
        'Days_Until_Due': int(days_until_due),
        'Estimated_Hours': float(estimated_hours),
        'Importance_Rating': int(importance_rating),
        'Task_Complexity': str(task_complexity),
        'Time_Slot': str(time_slot),
        'Past_Completion_Rate': float(past_completion_rate)
    }])

    # Transform through preprocessor
    features_transformed = preprocessor.transform(input_df)

    # Predict class & probabilities
    predicted_class = model.predict(features_transformed)[0]
    probabilities_raw = model.predict_proba(features_transformed)[0]
    classes = model.classes_

    probabilities = {
        cls: round(float(prob) * 100, 1)
        for cls, prob in zip(classes, probabilities_raw)
    }
    confidence = probabilities[predicted_class]

    # Smart scheduling recommendations based on urgency
    if predicted_class == 'High':
        alert_mode = "Loud Sound + Persistent Sticky Banner"
        frequency = "Every 3 Hours + Urgent Morning Alarm"
        badge_color = "danger"
        explanation = (
            f"High Urgency assigned because the task '{task_name}' is due in {days_until_due} "
            f"day(s) with high importance rating ({importance_rating}/5) and estimated duration of "
            f"{estimated_hours} hrs. Requires proactive alarms."
        )
    elif predicted_class == 'Medium':
        alert_mode = "Standard Tone + Push Notification"
        frequency = "Twice Daily (Morning & Evening Slot)"
        badge_color = "warning"
        explanation = (
            f"Medium Urgency assigned. The task '{task_name}' is due in {days_until_due} "
            f"day(s) with moderate importance ({importance_rating}/5). Recommended standard daily check-in."
        )
    else:
        alert_mode = "Gentle Chime / Silent Notification"
        frequency = "Single Reminder 24 Hours Before Due"
        badge_color = "success"
        explanation = (
            f"Low Urgency assigned. The deadline is {days_until_due} day(s) away with a low/manageable "
            f"effort requirement. A relaxed gentle notification will suffice."
        )

    return {
        'task_name': task_name,
        'category': category,
        'days_until_due': days_until_due,
        'estimated_hours': estimated_hours,
        'importance_rating': importance_rating,
        'task_complexity': task_complexity,
        'time_slot': time_slot,
        'past_completion_rate': past_completion_rate,
        'predicted_urgency': predicted_class,
        'confidence': confidence,
        'probabilities': probabilities,
        'alert_mode': alert_mode,
        'frequency': frequency,
        'explanation': explanation,
        'badge_color': badge_color
    }


if __name__ == '__main__':
    print("=" * 65)
    print("  SMART REMINDER - PREDICTION MODULE TEST")
    print("  Student: Shifa Baksare (AI & DS - 3rd Year)")
    print("=" * 65)

    test_samples = [
        {
            'task_name': 'Machine Learning Mini Project Submission',
            'category': 'Academic',
            'days_until_due': 1,
            'estimated_hours': 4.0,
            'importance_rating': 5,
            'task_complexity': 'High',
            'time_slot': 'Morning',
            'past_completion_rate': 0.90
        },
        {
            'task_name': 'Pay Electricity Utility Bill',
            'category': 'Financial',
            'days_until_due': 5,
            'estimated_hours': 0.5,
            'importance_rating': 3,
            'task_complexity': 'Low',
            'time_slot': 'Afternoon',
            'past_completion_rate': 0.85
        },
        {
            'task_name': 'Buy Weekly Groceries and Fruits',
            'category': 'Personal',
            'days_until_due': 12,
            'estimated_hours': 1.0,
            'importance_rating': 2,
            'task_complexity': 'Low',
            'time_slot': 'Evening',
            'past_completion_rate': 0.70
        }
    ]

    for i, sample in enumerate(test_samples, start=1):
        print(f"\n[Test Case #{i}] Task: {sample['task_name']}")
        result = predict_reminder(**sample)
        print(f"  * Predicted Urgency : {result['predicted_urgency']}")
        print(f"  * Confidence Score  : {result['confidence']}%")
        print(f"  * Probabilities     : {result['probabilities']}")
        print(f"  * Alert Mode        : {result['alert_mode']}")
        print(f"  * Frequency         : {result['frequency']}")
        print(f"  * Explanation       : {result['explanation']}")

    print("\n" + "=" * 65)
    print("  ALL TEST PREDICTIONS COMPLETED SUCCESSFULLY!")
    print("=" * 65)
