from htmlnode import ParentNode, LeafNode
from markdown_blocks import markdown_to_blocks, block_to_block_type
from split_nodes import text_to_textnodes
from textnode import TextNode

# takes markdown document and converts it into html nodes
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown) #list of strings of markdown paragraphs
    html_nodes = []
    for block in blocks:
        type = block_to_block_type(block)
        tag = block_type_to_tag(type)
        block = block_strip(block, type)

        if type == "code":
            html_nodes.append(LeafNode(tag, block))
            
        elif type == "unordered list" or type == "ordered list":
            list_items = block.rstrip("\n").split("\n")
            item_nodes = []
            for item in list_items:
                leaf_nodes = []
                if type == "ordered list":
                    item = item.lstrip("1234567890").removeprefix(". ")
                text_nodes = text_to_textnodes(item)
                for text_node in text_nodes:
                    leaf_nodes.append(text_node.text_node_to_html_node())
                item_nodes.append(ParentNode("li", leaf_nodes))
            html_nodes.append(ParentNode(tag, item_nodes))

        else:
            text_nodes = text_to_textnodes(block)
            leaf_nodes = []
            for text_node in text_nodes:
                leaf_nodes.append(text_node.text_node_to_html_node())
            parent_node = ParentNode(tag, leaf_nodes)
            html_nodes.append(parent_node)
    return ParentNode("div", html_nodes)

def block_type_to_tag(type):
    match type:
        case "heading":
            return "h1"
        case "code":
            return "code"
        case "quote":
            return "blockquote"
        case "unordered list":
            return "ul"
        case "ordered list":
            return "ol"
        case "paragraph":
            return "p"
        case _:
            raise Exception("not valid type")
    return "INVALID BLOCK TYPE"

def block_strip(block, type):
    split_block = block.split("\n")
    match type:
        case "heading":
            return block.lstrip("# ")
        case "code":
            return block.strip("`\n")
        case "quote":
            new_block = ""
            for line in split_block:
                new_block = f"{new_block}{line.lstrip(">").lstrip()}\n"
            return new_block
        case "unordered list":
            new_block = ""
            for line in split_block:
                new_block = new_block + line.lstrip("* ").lstrip("- ") + "\n"
            return new_block
        case _:
            return block