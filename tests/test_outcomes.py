import unittest
from value.outcomes import Outcome, summarize


class OutcomeTests(unittest.TestCase):
    def test_preserves_original_score_and_version(self):
        r = Outcome("sig-1","edge.value.v0.1",72.4,"t0","t1",True,False,True,True).record()
        self.assertEqual(r["original_score"], 72.4)
        self.assertEqual(r["value_version"], "edge.value.v0.1")
        self.assertIn("immutable", r["semantics"])

    def test_summary_is_descriptive(self):
        rows = [
            Outcome("a","v",60,"t0","t1",True,True,True,True).record(),
            Outcome("b","v",50,"t0","t1",True,False,False,False).record(),
        ]
        s = summarize(rows)
        self.assertEqual(s["assessed"], 2)
        self.assertEqual(s["decision_change_rate"], 0.5)
        self.assertIn("does not prove causal", s["warning"])

    def test_empty_calibration_is_valid(self):
        self.assertEqual(summarize([])["assessed"], 0)


if __name__ == "__main__":
    unittest.main()
