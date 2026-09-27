import unittest

from value.engine import Candidate, rank, score


def candidate(id="x", **overrides):
    base = dict(
        relevance=0.8,
        consequence=0.8,
        actionability=0.8,
        novelty=0.8,
        reliability=0.8,
        time_advantage=0.8,
    )
    base.update(overrides)
    return Candidate(id=id, **base)


class ValueEngineTests(unittest.TestCase):
    def test_score_is_bounded_and_inspectable(self):
        result = score(candidate())
        self.assertGreaterEqual(result["value_score"], 0)
        self.assertLessEqual(result["value_score"], 100)
        self.assertEqual(result["meaning"], "attention_priority_only")
        self.assertIn("factors", result)
        self.assertIn("penalties", result)

    def test_low_reliability_cannot_be_rescued_by_consequence(self):
        sensational = score(candidate("sensational", consequence=1, reliability=0))
        verified = score(candidate("verified", consequence=0.7, reliability=1))
        self.assertGreater(verified["value_score"], sensational["value_score"])

    def test_duplication_reduces_priority(self):
        fresh = score(candidate("fresh", duplication=0))
        repeated = score(candidate("repeated", duplication=1))
        self.assertGreater(fresh["value_score"], repeated["value_score"])

    def test_manipulation_risk_reduces_priority(self):
        clean = score(candidate("clean", manipulation_risk=0))
        risky = score(candidate("risky", manipulation_risk=1))
        self.assertGreater(clean["value_score"], risky["value_score"])

    def test_no_signal_is_valid_output(self):
        low = candidate(
            "low",
            relevance=0.1,
            consequence=0.1,
            actionability=0.1,
            novelty=0.1,
            reliability=0.1,
            time_advantage=0.1,
        )
        result = rank([low])
        self.assertEqual(result["state"], "NO_SIGNAL")
        self.assertEqual(result["items"], [])

    def test_ranking_is_deterministic_with_id_tiebreak(self):
        result = rank([candidate("b"), candidate("a")], threshold=0)
        self.assertEqual([x["id"] for x in result["items"]], ["a", "b"])

    def test_attention_budget_prevents_firehose(self):
        result = rank([candidate(str(i)) for i in range(25)], threshold=0)
        self.assertEqual(len(result["items"]), 10)
        self.assertEqual(result["eligible"], 25)
        self.assertEqual(result["suppressed_above_threshold"], 15)

    def test_rejects_out_of_range_inputs(self):
        with self.assertRaises(ValueError):
            score(candidate(relevance=1.1))


if __name__ == "__main__":
    unittest.main()
