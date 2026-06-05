import unittest

from rules import RULES
from expert_system import ExpertSystem


class TestExpertSystem(unittest.TestCase):

    def test_flu_diagnosis(self):

        expert = ExpertSystem(RULES)

        facts = [
            "fever",
            "cough",
            "body_pain"
        ]

        results = expert.forward_chain(facts)

        self.assertIn("flu", results)
        self.assertIn("severe_flu", results)
        self.assertIn("doctor_consultation", results)


if __name__ == "__main__":
    unittest.main()