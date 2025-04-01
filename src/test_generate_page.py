import unittest

from generate_page import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_title1(self):
        markdown = """
# Title

* milk
* eggs
* cheese
"""
        title = extract_title(markdown)
        ans = "Title"
        self.assertEqual(ans, title)
    
    def test_title2(self):
        markdown = """
# This title
# Not Title
* milk
* eggs
* cheese
# Also not title
"""
        title = extract_title(markdown)
        ans = "This title"
        self.assertEqual(ans, title)
    
    def test_title3(self):
        markdown = """
## Title

##Title

* milk
* eggs
* cheese
"""
        with self.assertRaises(ValueError):
            title = extract_title(markdown)