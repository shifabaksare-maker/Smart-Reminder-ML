"""
Unit tests for Smart Reminder Flask Application and REST API.
Author: Shifa Baksare (AI & Data Science, 3rd Year)
"""

import json
import unittest
from app import app


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_health_endpoint(self):
        """GET /health should return 200 with healthy status."""
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'healthy')
        self.assertIn('author', data)

    def test_index_get(self):
        """GET / should render HTML page containing hero title."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn('SMART REMINDER', html)
        self.assertIn('Task Parameters', html)

    def test_index_post(self):
        """POST / with form data should return HTML with prediction results."""
        payload = {
            'task_name': 'Semester Lab Practical',
            'category': 'Academic',
            'days_until_due': '1',
            'estimated_hours': '3.0',
            'importance_rating': '5',
            'task_complexity': 'High',
            'time_slot': 'Morning',
            'past_completion_rate': '0.90'
        }
        response = self.client.post('/', data=payload)
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn('PREDICTED PRIORITY TIER', html)
        self.assertIn('Urgency', html)

    def test_api_predict_success(self):
        """POST /api/predict with valid JSON should return predicted urgency."""
        payload = {
            'task_name': 'Electricity Bill Payment',
            'category': 'Financial',
            'days_until_due': 4,
            'estimated_hours': 0.5,
            'importance_rating': 3,
            'task_complexity': 'Low',
            'time_slot': 'Afternoon',
            'past_completion_rate': 0.85
        }
        response = self.client.post(
            '/api/predict',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertIn('data', data)
        self.assertIn('predicted_urgency', data['data'])
        self.assertIn('probabilities', data['data'])
        self.assertIn('alert_mode', data['data'])

    def test_api_metrics(self):
        """GET /api/metrics should return model benchmarks and accuracy."""
        response = self.client.get('/api/metrics')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertIn('benchmarks', data)
        self.assertIn('hyperparameters', data)

    def test_api_presets(self):
        """GET /api/presets should return curated demonstration scenarios."""
        response = self.client.get('/api/presets')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertGreaterEqual(len(data['presets']), 3)

    def test_api_predict_options(self):
        """OPTIONS /api/predict should return 200 for CORS preflight."""
        response = self.client.open('/api/predict', method='OPTIONS')
        self.assertEqual(response.status_code, 200)

    def test_download_report(self):
        """GET /download/report should return PDF attachment."""
        response = self.client.get('/download/report')
        self.assertEqual(response.status_code, 200)
        self.assertIn('application/pdf', response.content_type)

    def test_download_presentation(self):
        """GET /download/presentation should return PPTX attachment."""
        response = self.client.get('/download/presentation')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            'application/vnd.openxmlformats-officedocument.presentationml.presentation' in response.content_type
            or 'application/octet-stream' in response.content_type
        )

    def test_serve_screenshot(self):
        """GET /screenshots/model_comparison.png should return PNG image."""
        response = self.client.get('/screenshots/model_comparison.png')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'image/png')


if __name__ == '__main__':
    unittest.main()
