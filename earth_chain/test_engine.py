import unittest
from engine import validate,report
class TestEngine(unittest.TestCase):
 def test_empty(self):
  self.assertEqual(report([])["observations"],0)
  self.assertFalse(report([])["prices_published"])
 def test_unverified_transaction_rejected(self):
  row=dict(id="x",timestamp="2026-10-04T12:00:00Z",commodity="hurd",kind="executed_transaction",price_usd_per_metric_ton=100,source="example",region="FL",evidence_url="https://example.org")
  self.assertEqual(len(validate([row])[1]),1)
 def test_valid_ask(self):
  row=dict(id="x",timestamp="2026-10-04T12:00:00Z",commodity="hurd",kind="ask",price_usd_per_metric_ton=100,source="example",region="FL",evidence_url="https://example.org")
  self.assertEqual(report([row])["counts"]["hurd"]["ask"],1)
if __name__=="__main__": unittest.main()
