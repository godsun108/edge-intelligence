import datetime as dt
import unittest

from value.bridge import build, derive


NOW = dt.datetime(2026, 9, 27, tzinfo=dt.timezone.utc)


def obs(**overrides):
    base = {
        "id": "1",
        "source": "USGS",
        "title": "Example",
        "url": "https://example.invalid/1",
        "observed_at": "2026-09-27T00:00:00Z",
        "retrieved_at": "2026-09-27T01:00:00Z",
        "tags": ["earth", "earthquake"],
        "data": {"magnitude": 6.0},
        "change": "new",
        "relevance": 0,
    }
    base.update(overrides)
    return base


class RadarValueBridgeTests(unittest.TestCase):
    def test_unknown_relevance_is_not_invented(self):
        candidate, reasons = derive(obs(relevance=0), now=NOW)
        self.assertEqual(candidate.relevance, 0)
        self.assertIn("no explicit RADAR relevance rule matched", reasons["relevance"])

    def test_primary_source_gets_reliability_not_truth(self):
        candidate, reasons = derive(obs(), now=NOW)
        self.assertEqual(candidate.reliability, 0.85)
        self.assertTrue(any("primary/public" in x for x in reasons["reliability"]))

    def test_same_observation_is_heavily_duplicate_penalized(self):
        same, _ = derive(obs(change="same"), now=NOW)
        fresh, _ = derive(obs(change="new"), now=NOW)
        self.assertGreater(same.duplication, fresh.duplication)

    def test_grant_deadline_creates_time_window_not_eligibility(self):
        grant = obs(
            source="Grants.gov",
            tags=["grant"],
            data={"closeDate": "10/02/2026"},
            change="new",
            relevance=25,
        )
        candidate, reasons = derive(grant, now=NOW)
        self.assertEqual(candidate.time_advantage, 0.9)
        self.assertLess(candidate.actionability, 0.5)
        self.assertTrue(any("eligibility not inferred" in x for x in reasons["actionability"]))

    def test_queue_preserves_source_provenance_and_derivation(self):
        snapshot = {
            "schema": "edge.radar.snapshot.v1",
            "generated_at": "2026-09-27T01:00:00Z",
            "observations": [obs(relevance=50)],
        }
        queue = build(snapshot, threshold=0, now=NOW)
        item = queue["items"][0]
        self.assertEqual(item["observation"]["source"], "USGS")
        self.assertIn("derivation_reasons", item)
        self.assertEqual(queue["input_schema"], "edge.radar.snapshot.v1")

    def test_cisa_kev_gets_deadline_semantics_without_asset_claim(self):
        kev = obs(
            source="CISA KEV",
            tags=["cybersecurity", "known exploited vulnerability"],
            data={"dueDate": "2026-10-02", "cve": "CVE-2099-1"},
            change="new",
            relevance=25,
        )
        candidate, reasons = derive(kev, now=NOW)
        self.assertEqual(candidate.consequence, 0.75)
        self.assertEqual(candidate.time_advantage, 0.85)
        self.assertTrue(any("applicability not inferred" in x for x in reasons["actionability"]))


if __name__ == "__main__":
    unittest.main()
