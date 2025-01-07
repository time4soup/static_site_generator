from textnode import TextNode
from markdown_blocks import block_to_block_type

def main():
    node = TextNode("text", "normal", None)
    node2 = TextNode("text", "normal")
    block = """1.  
2. 
4. """
    print(block_to_block_type(block))

main()