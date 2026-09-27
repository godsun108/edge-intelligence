import unittest
from value.corroboration import build, identifiers


class CorroborationTests(unittest.TestCase):
    def test_extracts_explicit_cve_only(self):
        self.assertEqual(identifiers({"title": "Patch CVE-2026-12345 now"}), ["CVE-2026-12345"])
        self.assertEqual(identifiers({"title": "similar security issue"}), [])

    def test_two_sources_are_corroborated(self):
        snap = {"observations": [
            {"id":"CVE-2026-12345","source":"A","title":"CVE-2026-12345","data":{}},
            {"id":"2","source":"B","title":"About CVE-2026-12345","data":{}},
        ]}
        group = build(snap)["groups"][0]
        self.assertTrue(group["corroborated"])
        self.assertEqual(group["independent_source_count"], 2)

    def test_duplicate_records_from_one_source_are_not_corroboration(self):
        snap = {"observations": [
            {"id":"1","source":"A","title":"CVE-2026-12345","data":{}},
            {"id":"2","source":"A","title":"CVE-2026-12345 update","data":{}},
        ]}
        self.assertFalse(build(snap)["groups"][0]["corroborated"])


if __name__ == "__main__":
    unittest.main()
