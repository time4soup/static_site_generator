import unittest

from split_nodes import split_nodes_delimiter, split_nodes_delimiter_helper, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
#split_nodes_delimiter tests
    def test_split_nodes(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        split_nodes = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL),
            ]
        self.assertEqual(new_nodes, split_nodes)
    
    def test_split_nodes2(self):
        node = TextNode("Text `code` Text `code` Text `code`", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        split_nodes = [
            TextNode("Text ", TextType.NORMAL), 
            TextNode("code", TextType.CODE), 
            TextNode(" Text ", TextType.NORMAL),
            TextNode("code", TextType.CODE), 
            TextNode(" Text ", TextType.NORMAL),
            TextNode("code", TextType.CODE), 
        ]
        self.assertEqual(new_nodes, split_nodes)
    
    def test_split_nodes3(self):
        node = TextNode("Text `code` Text `code` Text `code", TextType.NORMAL)
        split_nodes = [
            TextNode("Text ", TextType.NORMAL), 
            TextNode("code", TextType.CODE), 
            TextNode(" Text ", TextType.NORMAL),
            TextNode("code", TextType.CODE), 
            TextNode(" Text ", TextType.NORMAL),
            TextNode("code", TextType.CODE), 
        ]
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    
    def test_split_nodes4(self):
        node = TextNode("*italic* text *italic*", TextType.NORMAL)
        split_nodes = [
            TextNode("italic", TextType.ITALIC), 
            TextNode(" text ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC)
        ]
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, split_nodes)
    
    def test_split_nodes5(self):
        node = TextNode("  *text* `**bold***text*", TextType.NORMAL)
        split_nodes = [
            TextNode("  *text* `", TextType.NORMAL), 
            TextNode("bold", TextType.BOLD),
            TextNode("*text*", TextType.NORMAL)
        ]
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, split_nodes)
    
    def test_split_nodes6(self):
        node1 = TextNode("This is text with a `code block` word", TextType.NORMAL)
        node2 = TextNode("  *text* `bold`*text*", TextType.NORMAL)
        split_nodes = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL),
            TextNode("  *text* ", TextType.NORMAL), 
            TextNode("bold", TextType.CODE),
            TextNode("*text*", TextType.NORMAL)
        ]
        new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        self.assertEqual(new_nodes, split_nodes)

#test split_nodes_image
    def test_split_image(self):
        node = TextNode(
            "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
            )
        split_nodes = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev")
            ]
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, split_nodes)

    def test_split_image2(self):
        node = TextNode("I love images, here's one ![link words](link to image where)", TextType.NORMAL)
        split_nodes = [
            TextNode("I love images, here's one ", TextType.NORMAL), 
            TextNode("link words", TextType.IMAGE, "link to image where")
        ]
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, split_nodes)
    
    def test_split_image3(self):
        node = TextNode("I don't have an image sorry to dissapoint :<", TextType.NORMAL)
        split_nodes = [TextNode("I don't have an image sorry to dissapoint :<", TextType.NORMAL)]
        new_nodes = split_nodes_image([node])
        self.assertEqual(split_nodes, new_nodes)
    
    def test_split_image4(self):
        node1 = TextNode("I love images, here's one ![link words](link to image where)", TextType.NORMAL)
        node2 = TextNode(
            "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
            )
        split_nodes = [
            TextNode("I love images, here's one ", TextType.NORMAL), 
            TextNode("link words", TextType.IMAGE, "link to image where"),
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev")
        ]
        new_nodes = split_nodes_image([node1, node2])
        self.assertEqual(new_nodes, split_nodes)

#test split_nodes_links
    def test_split_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
            )
        split_nodes = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
            ]
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, split_nodes)

    def test_split_link2(self):
        node = TextNode("I love images, here's one [link words](link to image where)", TextType.NORMAL)
        split_nodes = [
            TextNode("I love images, here's one ", TextType.NORMAL), 
            TextNode("link words", TextType.LINK, "link to image where")
        ]
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, split_nodes)
    
    def test_split_link3(self):
        node = TextNode("I don't have an image sorry to dissapoint :<", TextType.NORMAL)
        split_nodes = [TextNode("I don't have an image sorry to dissapoint :<", TextType.NORMAL)]
        new_nodes = split_nodes_link([node])
    
    def test_split_link4(self):
        node1 = TextNode("I love images, here's one [link words](link to image where)", TextType.NORMAL)
        node2 = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
            )
        split_nodes = [
            TextNode("I love images, here's one ", TextType.NORMAL), 
            TextNode("link words", TextType.LINK, "link to image where"),
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
        ]
        new_nodes = split_nodes_link([node1, node2])
        self.assertEqual(new_nodes, split_nodes)

#test text_to_textnodes
    def test_text_2_node(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        split_nodes = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.NORMAL),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        new_nodes = text_to_textnodes(text)
        self.assertEqual(split_nodes, new_nodes)
    
    def test_text_2_node2(self):
        text = "`code` and *italic* and **bold** and ![image](url)"
        split_nodes = [
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.NORMAL), 
            TextNode("image", TextType.IMAGE, "url")
        ]
        new_nodes = text_to_textnodes(text)
        self.assertEqual(split_nodes, new_nodes)