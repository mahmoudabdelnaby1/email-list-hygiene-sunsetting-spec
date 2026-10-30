import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from list_scrubber import scrub_list

class TestScrub(unittest.TestCase):
    def test_scrub(self):
        in_c = Path(__file__).resolve().parent.parent / "examples" / "scrubbed_contacts_sample.csv"
        out_c = Path(__file__).resolve().parent.parent / "examples" / "clean_output.csv"
        c = scrub_list(str(in_c), str(out_c))
        self.assertGreaterEqual(c, 1)

if __name__ == "__main__":
    unittest.main()
