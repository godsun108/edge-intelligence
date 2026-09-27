import unittest
from radar.ingest import classify_change


class RadarChangeTests(unittest.TestCase):
    def test_new_source_is_baseline_not_new_event(self):
        self.assertEqual(classify_change("NEW","NEW:1","abc",{},{"OLD"}), "baseline")

    def test_new_record_on_known_source_is_new(self):
        self.assertEqual(classify_change("KNOWN","KNOWN:2","abc",{},{"KNOWN"}), "new")

    def test_changed_and_same_are_distinct(self):
        prev={"KNOWN:1":"old"}
        self.assertEqual(classify_change("KNOWN","KNOWN:1","new",prev,{"KNOWN"}), "changed")
        self.assertEqual(classify_change("KNOWN","KNOWN:1","old",prev,{"KNOWN"}), "same")


if __name__ == "__main__":
    unittest.main()
