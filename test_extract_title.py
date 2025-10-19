import unittest

from extract_title import extract_title
class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = """
# "Hello"
"""
        node = extract_title(md)
        self.assertEqual("Hello")

    def test_extract_title_no_header_1(self):
        md = """
"Hello"
"""
        node = extract_title(md)
        self.assertEqual("No header found.")

    def test_extract_title_no_header_2(self):
        md = """
"### Hello"
"""
        node = extract_title(md)
        self.assertEqual("No header found.")    