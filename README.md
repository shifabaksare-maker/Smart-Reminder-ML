# SMART REMINDER ⏰🤖
### Machine Learning Based Intelligent Reminder & Notification Urgency System
**Academic Mini Project** • **Department of Artificial Intelligence & Data Science (3rd Year)**  
**Author:** Shifa Baksare  

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Accuracy](https://img.shields.io/badge/Model%20Accuracy-88.0%25-success?style=for-the-badge)](file:///c:/Users/l/.antigravity-ide/Smart_Reminder_ML/screenshots/model_comparison.png)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Online%20(HTTPS)-success?style=for-the-badge&logo=cloudflare)](https://skirt-citizens-webster-antenna.trycloudflare.com)

---

## 🌐 Live Deployed Application Link

> 🔗 **Public URL:** [https://skirt-citizens-webster-antenna.trycloudflare.com](https://skirt-citizens-webster-antenna.trycloudflare.com)  
> 
> *Live HTTPS deployment powered by Cloudflare's Edge Network. Works across desktop, mobile, and tablets. Includes interactive audio synthesizers, REST API console, active task manager, and deliverable downloads.*

---

## 📌 Executive Summary

Traditional reminder and calendar applications (such as Google Keep, Apple Reminders, or Microsoft To Do) treat every notification identically: they fire a uniform audio-visual chime at a preset timestamp. This causes severe **notification fatigue** and **alert blindness**, causing users to dismiss or snooze critical deadlines.

**Smart Reminder** transforms dumb static timers into a context-aware prioritization engine. Using a supervised **Random Forest Classifier**, it evaluates 7 contextual parameters (deadline proximity, required duration, subjective importance, task complexity, category, time of day, and past completion reliability) to predict task urgency into three discrete tiers:
- 🚨 **High Urgency:** Loud persistent alarm, sticky banner alerts, frequent re-triggers (every 3 hours).
- ⚠️ **Medium Urgency:** Standard notification chimes, active daytime dispatch.
- ✅ **Low Urgency:** Silent notifications aggregated into daily or evening digest summaries.

---

## 📊 Key Highlights & Results

- **88.00% Test Accuracy** and **88.00% Weighted F1-Score** using Random Forest Classifier.
- **Zero Critical Misclassifications:** 0% High-urgency tasks misclassified as Low.
- **7-Attribute Contextual Preprocessing:** Robust `ColumnTransformer` with `StandardScaler` and `OneHotEncoder`.
- **Sub-2ms Inference Latency:** Preloaded serialized model for instant web and API responses.
- **One-Click Viva Voce Demo Presets:** Pre-configured academic, financial, medical, and personal scenarios for live examiner evaluation.

---

## 🏗️ System Architecture

```
+---------------------------------------------------------------------------------+
|                                USER INTERFACE LAYER                             |
|  - Modern Dark Glassmorphic Web Dashboard (Flask + HTML5 / CSS3)                |
|  - Dynamic Sliders for Days, Duration, and Rating with Live Feedback            |
|  - Viva Voce Scenario Presets (Medication Alert, Final Exam, Bill Payment)       |
|  - Programmatic REST API (/api/predict)                                         |
+---------------------------------------+-----------------------------------------+
                                        |
                                        v
+---------------------------------------------------------------------------------+
|                            DATA PREPROCESSING PIPELINE                          |
|  - Strict train_test_split (80/20 Stratified) with zero data leakage            |
|  - ColumnTransformer:                                                           |
|      * OneHotEncoder: [Category, Complexity, Time_Slot] (handle_unknown='ignore')|
|      * StandardScaler: [Days_Until_Due, Estimated_Hours, Importance_Rating]     |
+---------------------------------------+-----------------------------------------+
                                        |
                                        v
+---------------------------------------------------------------------------------+
|                            MACHINE LEARNING ENGINE                              |
|  - Algorithm: Random Forest Classifier (100 Trees, Max Depth 8)                 |
|  - Outputs Class Prediction: ['High', 'Medium', 'Low']                          |
|  - Computes Calibrated Probabilities: P(High), P(Medium), P(Low)                |
+---------------------------------------+-----------------------------------------+
                                        |
                                        v
+---------------------------------------------------------------------------------+
|                       DISPATCH & SCHEDULING ADAPTER                             |
|  - Maps predicted tier to acoustic mode, notification frequency & visual badge  |
|  - Provides Explainable AI (XAI) rationale for student viva defense             |
+---------------------------------------------------------------------------------+
```

---

## 📈 Model Performance & Evaluation

Three distinct machine learning models were trained and benchmarked on identical 80-20 stratified splits:

| Model Architecture | Test Accuracy | Weighted F1-Score | Inference Latency | Observations |
| :--- | :---: | :---: | :---: | :--- |
| **Logistic Regression** | 79.00% | 79.12% | 0.8 ms | Linear baseline; struggles with non-linear feature interactions |
| **Decision Tree (Depth 6)** | 83.50% | 83.45% | 0.9 ms | Captures non-linear rules; prone to single-tree variance |
| **Random Forest (100 Trees)** | **88.00%** | **88.00%** | **1.8 ms** | **Ensemble averaging prevents overfitting; optimal accuracy** |

### Evaluation Visualizations
The training pipeline automatically outputs high-resolution diagnostic charts:
- `screenshots/model_comparison.png`: Accuracy benchmark across classifiers.
- `screenshots/confusion_matrix.png`: Multi-class confusion matrix on test split.
- `screenshots/feature_importance.png`: Feature importance ranking (Days Until Due ~35%, Importance ~28%).

---

## 📂 Project Structure

```text
Smart_Reminder_ML/
├── dataset/
│   └── reminders.csv             # 1,000 multi-domain training samples
├── model/
│   ├── reminder_model.pkl        # Serialized Random Forest classifier
│   └── reminder_encoder.pkl      # Serialized ColumnTransformer preprocessor
├── presentation/
│   ├── generate_presentation.py  # Script generating viva PPTX via python-pptx
│   ├── Smart_Reminder_Presentation.pptx # 13-slide academic presentation
│   └── PRESENTATION_SLIDES.md    # Complete slide outline & speaking notes
├── report/
│   ├── generate_report.py        # Script generating 10+ page PDF report via ReportLab
│   ├── Smart_Reminder_Project_Report.pdf # Publication-quality PDF project report
│   └── PROJECT_REPORT.md         # Full academic project documentation in Markdown
├── screenshots/
│   ├── confusion_matrix.png      # Confusion matrix chart (300 DPI)
│   ├── feature_importance.png    # Top-10 feature importance chart (300 DPI)
│   └── model_comparison.png      # Model comparison chart (300 DPI)
├── static/
│   └── style.css                 # Premium dark-mode glassmorphic styling
├── templates/
│   └── index.html                # Responsive web app template with audio & reminders board
├── tests/
│   ├── test_model.py             # ML model, pipeline & edge cases unit tests
│   └── test_app.py               # Flask endpoints, REST API & download unit tests
├── app.py                        # Flask server (UI + REST API + CORS endpoints)
├── predict.py                    # Standalone inference module & scheduling logic
├── train_model.py                # End-to-end dataset generator, training & evaluation
├── requirements.txt              # Project dependencies
└── README.md                     # Comprehensive project documentation
```

---

## 🚀 Quickstart & Installation

### 1. Prerequisites
Ensure Python 3.10 or higher is installed on your system.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Train & Evaluate the ML Models
To re-generate the dataset, train all 3 classifiers, save the best model artifacts, and generate the evaluation plots:
```bash
python train_model.py
```

### 4. Run Automated Unit Test Suite
Verify that all ML pipeline, API endpoints, and artifact loaders pass:
```bash
python -m unittest discover tests
```

### 5. Run the Flask Web Application
Launch the interactive web server:
```bash
python app.py
```
Open your browser and navigate to:
```
http://127.0.0.1:5000
```

### 6. Generate Academic Presentation (.pptx)
```bash
python presentation/generate_presentation.py
```
Outputs: `presentation/Smart_Reminder_Presentation.pptx`

### 7. Generate Academic Project Report (.pdf)
```bash
python report/generate_report.py
```
Outputs: `report/Smart_Reminder_Project_Report.pdf`

---

## 🔌 REST API Documentation

### Predict Urgency Endpoint
- **URL:** `/api/predict`
- **Method:** `POST`
- **Content-Type:** `application/json`

#### Request Payload Example:
```json
{
  "task_name": "Final Year ML Mini Project Submission",
  "category": "Academic",
  "days_until_due": 1,
  "estimated_hours": 3.5,
  "importance_rating": 5,
  "task_complexity": "High",
  "time_slot": "Morning",
  "past_completion_rate": 0.85
}
```

#### Response Example:
```json
{
  "status": "success",
  "data": {
    "task_name": "Final Year ML Mini Project Submission",
    "category": "Academic",
    "days_until_due": 1,
    "predicted_urgency": "High",
    "confidence": 92.5,
    "probabilities": {
      "High": 92.5,
      "Medium": 6.3,
      "Low": 1.2
    },
    "alert_mode": "Loud Sound + Persistent Sticky Banner",
    "frequency": "Every 3 Hours + Urgent Morning Alarm",
    "badge_color": "danger",
    "explanation": "High Urgency assigned because the task 'Final Year ML Mini Project Submission' is due in 1 day(s), requires 3.5 hours, and holds high importance (5/5)."
  }
}
```

### Additional Endpoints:
- `GET /api/metrics`: Model benchmarks, accuracy metrics, and hyperparameters.
- `GET /api/presets`: Pre-configured viva voce demonstration scenarios.
- `GET /health`: Health status and deliverable artifact availability.
- `GET /download/report`: Download publication-quality PDF report.
- `GET /download/presentation`: Download 13-slide PowerPoint presentation (.pptx).

---

## 🎓 Viva Voce Frequently Asked Questions (Defense Guide)

### Q1: Why use Random Forest instead of Deep Learning?
> **Answer:** For structured tabular data with 7 features, Tree Ensembles (Random Forest) consistently match or exceed Deep Learning performance without severe overfitting, intensive hyperparameter tuning, or heavy compute requirements. Random Forest offers native feature interpretability (Gini importance) and sub-2 millisecond inference suitable for on-device mobile execution.

### Q2: How did you ensure zero data leakage during preprocessing?
> **Answer:** The dataset was split into training (80%) and testing (20%) sets using stratified sampling **before** fitting the `ColumnTransformer`. `StandardScaler` and `OneHotEncoder` were fitted strictly on `X_train`. The test set and all subsequent runtime predictions are solely transformed using the parameters learned from the training data.

### Q3: What happens when an unseen categorical value is passed?
> **Answer:** The `OneHotEncoder` was initialized with `handle_unknown='ignore'`. If an unknown category is received at inference time, it generates an all-zero vector rather than crashing the application.

### Q4: How does this project directly solve "Notification Fatigue"?
> **Answer:** By eliminating uniform alerts. Low urgency tasks are grouped into quiet daily or weekly digest summaries. Medium urgency tasks appear as badges during daytime hours. High urgency tasks trigger loud, persistent alarms with escalating cadences.

---

## 👩‍💻 Author & Academic Information

- **Candidate:** Shifa Baksare
- **Academic Degree:** Bachelor of Engineering in Artificial Intelligence & Data Science
- **Year of Study:** 3rd Year (B.E.)
- **Project Type:** Academic Mini Project / Capstone Defense
