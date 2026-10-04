import unittest
from export import build
class TestHandoff(unittest.TestCase):
 def test_empty_is_not_live(self):
  s,o,t=build([])
  self.assertEqual(o,[])
  self.assertEqual(t["status"],"LOCAL_ONLY")
  self.assertFalse(t["prices_published"])
 def test_consent_gate(self):
  row={"id":"q1","timestamp":"2026-10-04T12:00:00Z","commodity":"hurd","kind":"ask","price_usd_per_metric_ton":100,"source":"sample","region":"FL","evidence_url":"https://example.org"}
  self.assertEqual(build([row])[1],[])
  row["counterparty_contact_consent"]=True
  self.assertEqual(len(build([row])[1]),1)
  self.assertEqual(build([row])[1][0]["expected_cash_usd"],0)
if __name__=="__main__": unittest.main()
