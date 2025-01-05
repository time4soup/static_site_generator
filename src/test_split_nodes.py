import unittest

from split_nodes import split_nodes_delimiter, split_nodes_delimiter_helper
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
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