"""
Unit tests for Smart Reminder ML Model and Prediction Engine.
Author: Shifa Baksare (AI & Data Science, 3rd Year)
"""

import os
import unittest
import pandas as pd
import numpy as np
from predict import predict_reminder, load_artifacts, MODEL_PATH, ENCODER_PATH


class TestModelAndPrediction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.model, cls.encoder_dict = load_artifacts()

    def test_artifacts_exist(self):
        """Verify model and encoder files exist on disk."""
        self.assertTrue(os.path.exists(MODEL_PATH), "Model file reminder_model.pkl must exist")
        self.assertTrue(os.path.exists(ENCODER_PATH), "Encoder file reminder_encoder.pkl must exist")

    def test_encoder_contents(self):
        """Verify encoder dictionary contains expected components."""
        self.assertIn('preprocessor', self.encoder_dict)
        self.assertIn('cat_cols', self.encoder_dict)
        self.assertIn('num_cols', self.encoder_dict)
        self.assertIn('classes', self.encoder_dict)
        self.assertEqual(len(self.encoder_dict['classes']), 3)
        self.assertSetEqual(set(self.encoder_dict['classes']), {'High', 'Medium', 'Low'})

    def test_predict_standard_high_urgency(self):
        """A task due today with high importance and high duration should be High urgency."""
        res = predict_reminder(
            task_name="Emergency Viva Prep",
            category="Academic",
            days_until_due=0,
            estimated_hours=5.0,
            importance_rating=5,
            task_complexity="High",
            time_slot="Morning",
            past_completion_rate=0.85
        )
        self.assertEqual(res['predicted_urgency'], 'High')
        self.assertGreaterEqual(res['confidence'], 50.0)
        self.assertIn('probabilities', res)
        self.assertIn('High', res['probabilities'])
        self.assertIn('alert_mode', res)
        self.assertIn('frequency', res)
        self.assertIn('explanation', res)

    def test_predict_standard_low_urgency(self):
        """A task due in 14 days with low importance and low duration should be Low urgency."""
        res = predict_reminder(
            task_name="Clean bookshelf",
            category="Personal",
            days_until_due=14,
            estimated_hours=0.5,
            importance_rating=1,
            task_complexity="Low",
            time_slot="Evening",
            past_completion_rate=0.70
        )
        self.assertEqual(res['predicted_urgency'], 'Low')
        self.assertGreaterEqual(res['confidence'], 50.0)

    def test_probabilities_sum_to_100(self):
        """Verify multi-class probabilities sum to approximately 100%."""
        res = predict_reminder(
            task_name="Test Sum",
            category="Financial",
            days_until_due=3,
            estimated_hours=1.5,
            importance_rating=3,
            task_complexity="Medium",
            time_slot="Afternoon",
            past_completion_rate=0.80
        )
        prob_sum = sum(res['probabilities'].values())
        self.assertAlmostEqual(prob_sum, 100.0, delta=1.0)

    def test_unknown_categorical_handling(self):
        """OneHotEncoder handle_unknown='ignore' should gracefully handle unseen categories."""
        res = predict_reminder(
            task_name="Space Mission",
            category="Intergalactic",  # Unseen category
            days_until_due=2,
            estimated_hours=2.0,
            importance_rating=4,
            task_complexity="Extreme", # Unseen complexity
            time_slot="Midnight",      # Unseen slot
            past_completion_rate=0.50
        )
        self.assertIn(res['predicted_urgency'], ['High', 'Medium', 'Low'])
        self.assertIsInstance(res['confidence'], (int, float))

    def test_dataset_integrity(self):
        """Verify dataset CSV has 1,000 samples and correct columns."""
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(base_dir, 'dataset', 'reminders.csv')
        self.assertTrue(os.path.exists(csv_path), "Dataset CSV must exist")
        df = pd.read_csv(csv_path)
        self.assertEqual(len(df), 1000)
        expected_cols = {
            'Task_ID', 'Task_Name', 'Category', 'Days_Until_Due', 'Estimated_Hours',
            'Importance_Rating', 'Task_Complexity', 'Time_Slot', 'Past_Completion_Rate', 'Reminder_Urgency'
        }
        self.assertTrue(expected_cols.issubset(set(df.columns)))


if __name__ == '__main__':
    unittest.main()
