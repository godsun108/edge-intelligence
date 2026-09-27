import unittest
from radar.sources import normalize_cisa_kev, normalize_nvd


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

    def test_nvd_preserves_cve_and_cvss_provenance(self):
        payload={"vulnerabilities":[{"cve":{
          "id":"CVE-2099-0001","published":"2099-01-01T00:00:00.000",
          "lastModified":"2099-01-02T00:00:00.000","vulnStatus":"Analyzed",
          "descriptions":[{"lang":"en","value":"Example flaw"}],
          "metrics":{"cvssMetricV31":[{"cvssData":{"version":"3.1","baseScore":9.8,"baseSeverity":"CRITICAL"}}]}
        }}]}
        item=normalize_nvd(payload,"2099-01-03T00:00:00+00:00")[0]
        self.assertEqual(item["source"],"NIST NVD")
        self.assertEqual(item["id"],"CVE-2099-0001")
        self.assertEqual(item["data"]["cvss"]["baseScore"],9.8)


if __name__ == "__main__":
    unittest.main()
