import tempfile
import unittest
from pathlib import Path
from main import collect, version_tuple

class CompatTests(unittest.TestCase):
    def test_version_tuple(self):
        self.assertEqual(version_tuple("3.11"), (3, 11))
    def test_detects_new_stdlib_module(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "app.py"
            source.write_text("import tomllib\n", encoding="utf-8")
            findings = collect([folder], (3, 10))
            self.assertEqual(findings[0]["symbol"], "tomllib")
