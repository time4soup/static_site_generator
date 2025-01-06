import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
#tests for extract_markdown_images
    def test_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted = extract_markdown_images(text)
        correct = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extracted, correct)
    
    def test_images2(self):
        text = ""
        extracted = extract_markdown_images(text)
        correct = []
        self.assertEqual(extracted, correct)
    
    def test_images3(self):
        text = "blah blah text and such ![descriptive alt text](ferocious url grr) blah blah more text and such"
        extracted = extract_markdown_images(text)
        correct = [("descriptive alt text", "ferocious url grr")]
        self.assertEqual(extracted, correct)
    
    def test_images4(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted = extract_markdown_images(text)
        correct = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        self.assertEqual(extracted, correct)

#tests for extracts_markdown_links
    def test_links(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted = extract_markdown_links(text)
        correct = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extracted, correct)
    
    def test_links2(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted = extract_markdown_links(text)
        correct = [("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extracted, correct)
    
    def test_links3(self):
        text = ""
        extracted = extract_markdown_links(text)
        correct = []
        self.assertEqual(extracted, correct)
    
    def test_links4(self):
        text = "blah blah text and such [descriptive alt text](ferocious url grr) blah blah more text and such"
        extracted = extract_markdown_links(text)
        correct = [("descriptive alt text", "ferocious url grr")]
        self.assertEqual(extracted, correct)