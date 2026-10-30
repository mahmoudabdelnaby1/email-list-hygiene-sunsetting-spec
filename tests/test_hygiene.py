"""
Unit tests for Email Hygiene Auditor
"""
import unittest
from src.audit_inactives import audit_subscriber_list

class TestEmailHygiene(unittest.TestCase):
    def test_subscriber_segmentation(self):
        subs = [
            {"email": "act@test.com", "last_activity_date": "2026-09-25"},
            {"email": "risk@test.com", "last_activity_date": "2026-07-20"},
            {"email": "dead@test.com", "last_activity_date": "2025-01-01"}
        ]
        res = audit_subscriber_list(subs, "2026-10-01")
        self.assertEqual(res["counts"]["active"], 1)
        self.assertEqual(res["counts"]["at_risk"], 1)
        self.assertEqual(res["counts"]["suppress"], 1)

if __name__ == "__main__":
    unittest.main()
