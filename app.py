"""
SMART REMINDER – Machine Learning Based Reminder System
Author: Shifa Baksare (AI & Data Science, 3rd Year)

File: app.py
Description: Flask Web Application serving the interactive UI and ML prediction engine.
"""

import os
import sys
from flask import Flask, render_template, request, jsonify, send_from_directory, abort

# Set UTF-8 encoding for stdout
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Import inference logic
from predict import predict_reminder, load_artifacts

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = os.path.join(BASE_DIR, 'report')
PRESENTATION_DIR = os.path.join(BASE_DIR, 'presentation')
SCREENSHOTS_DIR = os.path.join(BASE_DIR, 'screenshots')

# Preload model on startup to ensure no latency on first request
try:
    load_artifacts()
    print("[OK] ML Model and Encoder loaded successfully.")
except Exception as e:
    print(f"[WARNING] Could not preload artifacts ({e}). Run train_model.py first.")


@app.route('/', methods=['GET', 'POST'])
def index():
    form_data = {
        'task_name': 'Final Year ML Mini Project Submission',
        'category': 'Academic',
        'days_until_due': 1,
        'estimated_hours': 3.5,
        'importance_rating': 5,
        'task_complexity': 'High',
        'time_slot': 'Morning',
        'past_completion_rate': 0.85
    }

    if request.method == 'POST':
        form_data = {
            'task_name': request.form.get('task_name', 'Task').strip(),
            'category': request.form.get('category', 'Academic'),
            'days_until_due': int(request.form.get('days_until_due', 1)),
            'estimated_hours': float(request.form.get('estimated_hours', 1.0)),
            'importance_rating': int(request.form.get('importance_rating', 3)),
            'task_complexity': request.form.get('task_complexity', 'Medium'),
            'time_slot': request.form.get('time_slot', 'Morning'),
            'past_completion_rate': float(request.form.get('past_completion_rate', 0.80))
        }

    try:
        prediction_result = predict_reminder(
            task_name=form_data['task_name'],
            category=form_data['category'],
            days_until_due=form_data['days_until_due'],
            estimated_hours=form_data['estimated_hours'],
            importance_rating=form_data['importance_rating'],
            task_complexity=form_data['task_complexity'],
            time_slot=form_data['time_slot'],
            past_completion_rate=form_data['past_completion_rate']
        )
    except Exception as err:
        prediction_result = {
            'error': f"Prediction Error: {str(err)}"
        }

    return render_template('index.html', result=prediction_result, form_data=form_data)


@app.after_request
def add_cors_headers(response):
    """Enable Cross-Origin Resource Sharing for API consumers."""
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
    return response


@app.route('/api/predict', methods=['POST', 'OPTIONS'])
def api_predict():
    """REST API endpoint for programmatic inference with CORS support."""
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok'}), 200

    try:
        data = request.get_json(force=True) if request.is_json or request.data else {}
        result = predict_reminder(
            task_name=data.get('task_name', 'Unnamed Task'),
            category=data.get('category', 'Personal'),
            days_until_due=int(data.get('days_until_due', 2)),
            estimated_hours=float(data.get('estimated_hours', 1.0)),
            importance_rating=int(data.get('importance_rating', 3)),
            task_complexity=data.get('task_complexity', 'Medium'),
            time_slot=data.get('time_slot', 'Morning'),
            past_completion_rate=float(data.get('past_completion_rate', 0.8))
        )
        return jsonify({'status': 'success', 'data': result})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400


@app.route('/api/metrics', methods=['GET'])
def api_metrics():
    """Returns academic benchmarks and ML model performance metrics."""
    return jsonify({
        'status': 'success',
        'model_name': 'Random Forest Classifier',
        'hyperparameters': {
            'n_estimators': 100,
            'max_depth': 8,
            'criterion': 'gini',
            'random_state': 42
        },
        'benchmarks': [
            {'model': 'Random Forest', 'accuracy': 88.00, 'weighted_f1': 87.95, 'latency_ms': 1.8, 'selected': True},
            {'model': 'Logistic Regression', 'accuracy': 89.00, 'weighted_f1': 89.00, 'latency_ms': 0.8, 'selected': False},
            {'model': 'Decision Tree', 'accuracy': 86.50, 'weighted_f1': 86.45, 'latency_ms': 0.9, 'selected': False}
        ],
        'dataset_summary': {
            'total_samples': 1000,
            'train_samples': 800,
            'test_samples': 200,
            'features_count': 7,
            'classes': ['High', 'Medium', 'Low'],
            'target': 'Reminder_Urgency'
        }
    })


@app.route('/api/presets', methods=['GET'])
def api_presets():
    """Returns curated viva voce demonstration scenarios."""
    return jsonify({
        'status': 'success',
        'presets': [
            {
                'id': 'viva_high',
                'name': '🎓 Final ML Lab Viva & Report',
                'category': 'Academic',
                'days_until_due': 1,
                'estimated_hours': 4.0,
                'importance_rating': 5,
                'task_complexity': 'High',
                'time_slot': 'Morning',
                'past_completion_rate': 0.85,
                'expected_tier': 'High'
            },
            {
                'id': 'med_high',
                'name': '💊 Take Morning Blood Pressure Medication',
                'category': 'Health',
                'days_until_due': 0,
                'estimated_hours': 0.25,
                'importance_rating': 5,
                'task_complexity': 'Low',
                'time_slot': 'Morning',
                'past_completion_rate': 0.95,
                'expected_tier': 'High'
            },
            {
                'id': 'bill_med',
                'name': '💳 Pay Electricity & Wi-Fi Bill',
                'category': 'Financial',
                'days_until_due': 4,
                'estimated_hours': 0.5,
                'importance_rating': 3,
                'task_complexity': 'Medium',
                'time_slot': 'Afternoon',
                'past_completion_rate': 0.90,
                'expected_tier': 'Medium'
            },
            {
                'id': 'grocery_low',
                'name': '🛒 Weekly Grocery & Fruit Shopping',
                'category': 'Personal',
                'days_until_due': 10,
                'estimated_hours': 1.5,
                'importance_rating': 2,
                'task_complexity': 'Low',
                'time_slot': 'Evening',
                'past_completion_rate': 0.75,
                'expected_tier': 'Low'
            }
        ]
    })


@app.route('/download/report', methods=['GET'])
def download_report():
    """Download academic project report PDF."""
    pdf_filename = 'Smart_Reminder_Project_Report.pdf'
    if not os.path.exists(os.path.join(REPORT_DIR, pdf_filename)):
        abort(404, description="Report PDF not found. Run report/generate_report.py first.")
    return send_from_directory(REPORT_DIR, pdf_filename, as_attachment=True)


@app.route('/download/presentation', methods=['GET'])
def download_presentation():
    """Download academic presentation PPTX."""
    pptx_filename = 'Smart_Reminder_Presentation.pptx'
    if not os.path.exists(os.path.join(PRESENTATION_DIR, pptx_filename)):
        abort(404, description="Presentation PPTX not found. Run presentation/generate_presentation.py first.")
    return send_from_directory(PRESENTATION_DIR, pptx_filename, as_attachment=True)


@app.route('/screenshots/<path:filename>', methods=['GET'])
def serve_screenshot(filename):
    """Serve evaluation charts."""
    return send_from_directory(SCREENSHOTS_DIR, filename)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'project': 'Smart Reminder - ML Based Reminder System',
        'author': 'Shifa Baksare',
        'branch': 'AI & Data Science (3rd Year)',
        'report_available': os.path.exists(os.path.join(REPORT_DIR, 'Smart_Reminder_Project_Report.pdf')),
        'presentation_available': os.path.exists(os.path.join(PRESENTATION_DIR, 'Smart_Reminder_Presentation.pptx'))
    })


if __name__ == '__main__':
    # Run development server
    port = int(os.environ.get('PORT', 5000))
    print(f"[OK] Starting Flask Application on http://127.0.0.1:{port}")
    app.run(host='127.0.0.1', port=port, debug=True)

