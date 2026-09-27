import pathlib
import unittest


class SourceInventoryTests(unittest.TestCase):
    def test_ingest_declares_authoritative_source_families(self):
        text=pathlib.Path("radar/ingest.py").read_text()
        for source in ("USGS","Grants.gov","NASA EONET","CISA KEV","NIST NVD","Federal Register"):
            self.assertIn(source,text)


if __name__=="__main__": unittest.main()
