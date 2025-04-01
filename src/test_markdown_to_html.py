import unittest

from markdown_to_html import markdown_to_html_node
from htmlnode import ParentNode, LeafNode

class TestMarkdownToHtml(unittest.TestCase):
    # test markdown_to_html
    def test_markdown_to_html1(self):
        markdown = """
This is a **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here
"""
        html = markdown_to_html_node(markdown)
        goal = ParentNode(
            "div", 
            [ 
                ParentNode(
                    "p",
                    [ 
                        LeafNode(None, "This is a "), 
                        LeafNode("b", "bolded"), 
                        LeafNode(None, " paragraph\ntext in a p\ntag here")
                    ], 
                ), 
                ParentNode(
                    "p",
                    [ 
                        LeafNode(None, "This is another paragraph with "), 
                        LeafNode("i", "italic"), 
                        LeafNode(None, " text and "), 
                        LeafNode("code", "code"), 
                        LeafNode(None, " here")
                    ], 
                )
            ])
        self.assertEqual(goal, html)
    
    def test_markdown_to_html2(self):
        markdown = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        html = markdown_to_html_node(markdown)
        goal = ParentNode(
            "div", 
            [ 
                LeafNode("code", "This is text that _should_ remain\nthe **same** even with inline stuff") 
            ])
        self.assertEqual(goal, html)
    
    def test_markdown_to_html3(self):
        markdown = """
## Title
    
1. thing
2. thinger
3. thingest

>smart words?
>-me

- milk
- eggs
- cheese
"""
        html = markdown_to_html_node(markdown)
        goal = ParentNode(
            "div", 
            [ 
                ParentNode(
                    "h1",
                    [
                        LeafNode(None, "Title")
                    ]), 
                ParentNode(
                    "ol", 
                    [
                        LeafNode("li", "1. thing"), 
                        LeafNode("li", "2. thinger"), 
                        LeafNode("li", "3. thingest")
                    ]),
                ParentNode(
                    "blockquote", 
                    [
                        LeafNode(None, "smart words?\n-me")
                    ]), 
                ParentNode(
                    "ul", 
                    [
                        LeafNode("li", "milk"), 
                        LeafNode("li", "eggs"), 
                        LeafNode("li", "cheese")
                    ]
                )
            ])
        self.assertEqual(goal, html)

    def test_markdown_to_html2(self):
        markdown = """
![img text](Isolated.png)

[link text](Duck.com)
"""
        html = markdown_to_html_node(markdown)
        goal = ParentNode(
            "div", 
            [
                ParentNode(
                    "p", 
                    [LeafNode("img", "", {"src": "Isolated.png", "alt": "img text"})]
                ), 
                ParentNode(
                    "p", 
                    [LeafNode("a", "link text", {"href": "Duck.com"})]
                )
            ])
        self.assertEqual(goal, html)