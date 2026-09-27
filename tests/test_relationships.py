import unittest
from value.relationships import build, entities, diff


class RelationshipTests(unittest.TestCase):
    def test_extracts_only_explicit_entities(self):
        o={"id":"CVE-2026-12345","title":"Issue","data":{"vendor":"Acme","product":"Widget"}}
        self.assertIn(("cve","CVE-2026-12345"),entities(o))
        self.assertIn(("vendor","Acme"),entities(o))
        self.assertNotIn(("vendor","Other"),entities(o))

    def test_cooccurrence_is_labeled_association_not_causation(self):
        g=build({"observations":[{"id":"CVE-2026-12345","source":"A","title":"Issue","data":{"vendor":"Acme","product":"Widget"}}]})
        self.assertGreater(len(g["edges"]),0)
        self.assertIn("not causation",g["semantics"])

    def test_independent_sources_count_distinctly(self):
        obs=[
          {"id":"CVE-2026-12345","source":"A","title":"Issue","data":{"vendor":"Acme"}},
          {"id":"CVE-2026-12345","source":"B","title":"Issue","data":{"vendor":"Acme"}},
        ]
        edges=build({"observations":obs})["edges"]
        edge=next(e for e in edges if "cve:CVE-2026-12345" in (e["left"],e["right"]))
        self.assertEqual(edge["independent_source_count"],2)

    def test_diff_reports_only_new_explicit_edges(self):
        old=build({"observations":[{"id":"CVE-2026-12345","source":"A","title":"Issue","data":{"vendor":"Acme"}}]})
        new=build({"observations":[
          {"id":"CVE-2026-12345","source":"A","title":"Issue","data":{"vendor":"Acme"}},
          {"id":"CVE-2026-99999","source":"A","title":"Other","data":{"vendor":"Other"}},
        ]})
        d=diff(old,new)
        self.assertGreater(d["new_edge_count"],0)
        self.assertIn("not evidence of causality",d["semantics"])


if __name__=="__main__": unittest.main()
