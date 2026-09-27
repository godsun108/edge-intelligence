import unittest
from radar.sources import normalize_cisa_kev


class SourceAdapterTests(unittest.TestCase):
    def test_cisa_kev_preserves_security_provenance(self):
        payload = {"vulnerabilities": [{
            "cveID": "CVE-2099-0001",
            "vendorProject": "Example",
            "product": "Widget",
            "vulnerabilityName": "Example vulnerability",
            "dateAdded": "2099-01-01",
            "dueDate": "2099-01-22",
            "knownRansomwareCampaignUse": "Known",
            "requiredAction": "Apply vendor mitigations",
        }]}
        item = normalize_cisa_kev(payload, "2099-01-02T00:00:00+00:00")[0]
        self.assertEqual(item["source"], "CISA KEV")
        self.assertEqual(item["id"], "CVE-2099-0001")
        self.assertEqual(item["data"]["dueDate"], "2099-01-22")
        self.assertIn("known exploited vulnerability", item["tags"])


if __name__ == "__main__":
    unittest.main()
