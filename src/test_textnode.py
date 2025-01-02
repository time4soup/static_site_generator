import unittest

from textnode import TextNode, TextType
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
###TextNode tests
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_text_not_eq(self):
        node = TextNode("text", "bold")
        node2 = TextNode("words", "bold")
        self.assertFalse(node == node2)
    
    def test_text_type_not_eq(self):
        node = TextNode("text", "bold")
        node2 = TextNode("text", "normal")
        self.assertFalse(node == node2)
    
    def test_eq2(self):
        node = TextNode("text", "bold", "url")
        node2 = TextNode("text", "bold", "url")
        self.assertEqual(node, node2)
    
    def test_to_html_node_bold(self):
        node = TextNode("text", "bold")
        node = node.text_node_to_html_node()
        self.assertTrue(node == LeafNode("b", "text"))
    
    def test_to_html_node_normal(self):
        node = TextNode("text", "normal")
        node = node.text_node_to_html_node()
        self.assertTrue(node == LeafNode(None, "text"))
    
    def test_to_html_node_italic(self):
        node = TextNode("text", "italic")
        node = node.text_node_to_html_node()
        self.assertTrue(node == LeafNode("i", "text"))
    
    def test_to_html_node_code(self):
        node = TextNode("text", "code")
        node = node.text_node_to_html_node()
        self.assertTrue(node == LeafNode("code", "text"))
    
    def test_to_html_node_link(self):
        node = TextNode("text", "link", "url")
        node = node.text_node_to_html_node()
        self.assertTrue(node == LeafNode("a", "text", {"href": "url"}))
    
    def test_to_html_node_image(self):
        node = TextNode("text", "image", "url")
        node = node.text_node_to_html_node()
        self.assertTrue(node == LeafNode("img", "", {"src": "url", "alt": "text"}))


if __name__ == "__main__":
    unittest.main()
