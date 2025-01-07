import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type

class TestMarkdownToBlocks(unittest.TestCase):
    #test markdown_to_blocks
    def test_markdown_2_blocks(self):
        markdown = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """
        test_blocks = markdown_to_blocks(markdown)
        true_blocks = [
            "# This is a heading", 
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", 
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
            ]
        self.assertEqual(test_blocks, true_blocks)
    
    def test_markddown_2_blocks(self):
        markdown = """
        
        
        #header
        #another header
        # a third header!!!
        
        
        * list
        * of 
        * stuff"""
        test_blocks = markdown_to_blocks(markdown)
        true_blocks = [
            "#header\n#another header\n# a third header!!!", 
            "* list\n* of\n* stuff"""
        ]
        self.assertEqual(test_blocks, true_blocks)
    
    def test_markdown_2_blocks3(self):
        markdown = """
        
        
        
        
        """
        test_blocks = markdown_to_blocks(markdown)
        true_blocks = []
        self.assertEqual(test_blocks, true_blocks)

    #test block_to_blocktype
    def test_block_2_type(self):
        block = """# heading"""
        test_type = block_to_block_type(block)
        true_type = "heading"
        self.assertEqual(test_type, true_type)
    
    def test_block_2_type2(self):
        block = """###### heading"""
        test_type = block_to_block_type(block)
        true_type = "heading"
        self.assertEqual(test_type, true_type)
    
    def test_block_2_type3(self):
        block = """#######"""
        test_type = block_to_block_type(block)
        true_type = "paragraph"
        self.assertEqual(test_type, true_type)
    
    def test_block_2_type4(self):
        block = """``` stuff and stuff ```"""
        test_type = block_to_block_type(block)
        true_type = "code"
        self.assertEqual(test_type, true_type)
    
    def test_block_2_type5(self):
        block = """``` `````````"""
        test_type = block_to_block_type(block)
        true_type = "code"
        self.assertEqual(test_type, true_type)
    
    def test_block_2_type6(self):
        block = """`` ``"""
        test_type = block_to_block_type(block)
        true_type = "paragraph"
        self.assertEqual(test_type, true_type)
    
    def test_block_2_type7(self):
        block = """> word"""
        test_type = block_to_block_type(block)
        true_type = "quote"
        self.assertEqual(test_type, true_type)
    
    def test_block_2_type8(self):
        block = """> 
> 
> word"""
        test_type = block_to_block_type(block)
        true_type = "quote"
        self.assertEqual(test_type, true_type)
    
    def test_block_2_type9(self):
        block = """>>>"""
        test_type = block_to_block_type(block)
        true_type = "quote"
        self.assertEqual(test_type, true_type)
    
    def test_block_2_type10(self):
        block = """* """
        test_type = block_to_block_type(block)
        true_type = "unordered list"
        self.assertEqual(test_type, true_type)
    
    def test_block_2_type11(self):
        block = """- 
* 
- """
        test_type = block_to_block_type(block)
        true_type = "unordered list"
        self.assertEqual(test_type, true_type)
    
    def test_block_2_type12(self):
        block = """*
-"""
        test_type = block_to_block_type(block)
        true_type = "paragraph"
        self.assertEqual(test_type, true_type)
    
    def test_block_2_type13(self):
        block = """1.  """
        test_type = block_to_block_type(block)
        true_type = "ordered list"
        self.assertEqual(test_type, true_type)
    
    def test_block_2_type14(self):
        block = """1. 
2. 
3. 
4. """
        test_type = block_to_block_type(block)
        true_type = "ordered list"
        self.assertEqual(test_type, true_type)
    
    def test_block_2_type15(self):
        block = """1. 
2. 
4. """
        test_type = block_to_block_type(block)
        true_type = "paragraph"
        self.assertEqual(test_type, true_type)
    
    def test_block_2_type16(self):
        block = """words
        words"""
        test_type = block_to_block_type(block)
        true_type = "paragraph"
        self.assertEqual(test_type, true_type)