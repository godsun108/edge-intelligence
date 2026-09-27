import unittest
from value.lab import freeze


class ValueLabTests(unittest.TestCase):
    def snapshot(self):
        return {"schema":"edge.radar.snapshot.v1","generated_at":"t0","observations":[
          {"id":"1","source":"A","title":"one","observed_at":"2026-01-01","change":"same","relevance":0,"data":{}},
          {"id":"2","source":"B","title":"two","observed_at":"2026-01-02","change":"new","relevance":25,"data":{}},
        ]}

    def test_freezes_all_candidates_not_only_signals(self):
        lab=freeze(self.snapshot())
        self.assertEqual(lab["candidate_count"],2)
        self.assertEqual(len(lab["candidates"]),2)
        self.assertTrue(lab["rules"]["prospective_only"])
        self.assertIn("value_selected",lab)

    def test_baselines_are_deterministic_and_bounded(self):
        lab=freeze(self.snapshot(),budget=1)
        self.assertEqual(len(lab["baselines"]["newest_first"]),1)
        self.assertEqual(lab["baselines"]["newest_first"][0],"B:2")

    def test_silence_is_preserved_as_value_policy(self):
        lab=freeze({"schema":"edge.radar.snapshot.v1","observations":[{"id":"1","source":"A","title":"quiet","change":"same","relevance":0,"data":{}}]})
        self.assertEqual(lab["value_selected"],[])

    def test_lab_is_not_attention_queue(self):
        self.assertIn("not an attention queue",freeze(self.snapshot())["semantics"])


if __name__=="__main__": unittest.main()
