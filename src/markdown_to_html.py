from htmlnode import HTMLNode, ParentNode, LeafNode
from markdown_blocks import markdown_to_blocks, block_to_block_type
from split_nodes import text_to_textnodes

'''
general flow (markdown -> html)
markdown -> blocks:
    markdown_blocks.py "markdown_to_blocks" and "block_to_block_type" for info to make text nodes
block -> text node:
    split_nodes "text_to_text_nodes" to split markdown blocks into text nodes
text node -> html node:
    textnode "text_node_to_html" method
html node -> raw html:
    htmlnode.py "to_html" method
'''
# takes markdown document and converts it into html nodes
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown) #list of strings of markdown
    html_nodes = []
    for block in blocks:
        type = block_to_block_type(block)
        match type:
            case "heading":
                tag = "h1"
            case "code":
                tag = "code"
            case "quote":
                tag = "blockquote"
            case "unordered list":
                tag = "ul"
            case "ordered list":
                tag = "ol"
            case "paragraph":
                tag = "p"
            case _:
                raise Exception("not valid type")
        if type == "paragraph":
            text_nodes = text_to_textnodes(block)
            for text_node in text_nodes:
                html_nodes.append(text_node.text_node_to_html_node())
        else:
            html_nodes.append(LeafNode(tag, block))
        

def paragraph_to_html_nodes(paragraph):
    pass # !!! finish fxn and implement call in markdown to html fxn