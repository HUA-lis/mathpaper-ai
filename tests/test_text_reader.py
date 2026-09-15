import tempfile
import unittest
from pathlib import Path

from src.text_reader import read_txt_file


class TestTextReader(unittest.TestCase):
    def test_read_existing_txt_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "sample.txt"
            file_path.write_text("Hello MathPaper AI", encoding="utf-8")

            content = read_txt_file(file_path)

            self.assertEqual(content, "Hello MathPaper AI")

    def test_read_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            read_txt_file("file_that_does_not_exist.txt")


if __name__ == "__main__":
    unittest.main()
