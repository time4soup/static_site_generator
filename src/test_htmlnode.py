import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
###HTMLNode tests
    def test_eq_value(self):
        node = HTMLNode("This is a text node", "bold")
        node2 = HTMLNode("This is a text node", "bold")
        self.assertEqual(node.value, "bold")
    
    def test_props_to_html(self):
        node = HTMLNode("b", "cheese", props={"key1":"val1", "key2":"val2"})
        val = node.props_to_html()
        self.assertEqual(val, " key1='val1' key2='val2'")
    
    def test_no_params(self):
        node = HTMLNode()
        val = node.props_to_html()
        self.assertEqual(val, "")

### LeafNode tests    
    def test_p_leaf(self):
        leaf = LeafNode("p", "paragraph text")
        p_html = "<p>paragraph text</p>"
        self.assertEqual(p_html, leaf.to_html())
    
    def test_b_leaf(self):
        leaf = LeafNode("b", "bold text")
        b_html = "<b>bold text</b>"
        self.assertEqual(b_html, leaf.to_html())
    
    def test_a_leaf(self):
        leaf = LeafNode("a", "link text", {"href": "https://youtube.com"})
        a_html = "<a href=\"https://youtube.com\">link text</a>"
        self.assertEqual(a_html, leaf.to_html())

### ParentNode tests
    def test_parent_node1(self):
        parent = ParentNode(
            "p",
            [
                LeafNode("b", "bold text"),
                LeafNode(None, "normal text"), 
                LeafNode("i", "italic text"), 
                LeafNode("a", "link text", {"href": "https://youtube.com"})
            ]
        )
        parent_html = "<p><b>bold text</b>normal text<i>italic text</i><a href=\"https://youtube.com\">link text</a></p>"
        self.assertEqual(parent_html, parent.to_html())
    
    def test_parent_node2(self):
        parent = ParentNode(
            "p", 
            [LeafNode("b", "bold text")]
        )
        parent_html = "<p><b>bold text</b></p>"
        self.assertEqual(parent_html, parent.to_html())
    
    def test_parent_node3(self):
        parent = ParentNode(
            "a",
            [LeafNode("i", "italic text")], 
            {"href": "link url"}
        )
        parent_html = "<a href=\"link url\"><i>italic text</i></a>"
        self.assertEqual(parent_html, parent.to_html())
    
    def test_parent_node4(self):
        parent = ParentNode(
            "p", 
            [
                LeafNode("b", "bold text"), 
                ParentNode(
                    "a", 
                    [
                        LeafNode("p", "paragraph text"), 
                        LeafNode("p", "paragraph text"), 
                        LeafNode("p", "paragraph text")
                    ], 
                    {"href": "link url"}
                )
            ]
        )
        parent_html = "<p><b>bold text</b><a href=\"link url\"><p>paragraph text</p><p>paragraph text</p><p>paragraph text</p></a></p>"
        self.assertEqual(parent_html, parent.to_html())

if __name__ == "__main__":
    unittest.main()