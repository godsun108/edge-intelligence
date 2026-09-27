import unittest
from value.lab_report import report


class LabReportTests(unittest.TestCase):
    def freeze(self):
        return {"candidate_count":2,"attention_budget":1,"candidates":[{"id":"A:1"},{"id":"B:2"}],"baselines":{"newest_first":["B:2"]}}

    def test_no_outcomes_means_insufficient_not_winner(self):
        r=report(self.freeze(),[])
        self.assertEqual(r["status"],"INSUFFICIENT_OUTCOMES")
        self.assertIn("No method is declared superior",r["warning"])

    def test_reports_hits_without_ranking_methods(self):
        outcomes=[{"signal_id":"A:1","consequence_observed":True,"timely":True}]
        r=report(self.freeze(),outcomes)
        self.assertEqual(r["methods"]["value_top_budget"]["consequence_hits"],1)
        self.assertNotIn("winner",r)


if __name__=="__main__": unittest.main()
