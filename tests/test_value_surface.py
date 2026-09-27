import pathlib
import unittest


class ValueSurfaceTests(unittest.TestCase):
    def test_console_consumes_canonical_value_artifact(self):
        html = pathlib.Path("index.html").read_text()
        js = pathlib.Path("app.js").read_text()
        self.assertIn('id="value-status"', html)
        self.assertIn("value/data/latest.json", js)
        self.assertIn("NO SIGNAL", js)
        self.assertIn("NO SIGNAL IS BEING FABRICATED", js)


if __name__ == "__main__":
    unittest.main()
