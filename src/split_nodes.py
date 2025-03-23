from textnode import TextNode, TextType
from extract_markdown import extract_markdown_links, extract_markdown_images

#checks if input nodes need to be split, calls helper if splitting required
#input: list of TextNodes, delimiter string, text type of inside markdown (text_type Enum)
#output: list of new nodes (TextNodes)
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if old_nodes is None or len(old_nodes) == 0:
        raise Exception("cannot split nodes without nodes")
    new_nodes = []
    for node in old_nodes:
        if node.text_type.value != "normal":
            new_nodes.append(node)
        elif node.text.count(delimiter) == 0:
            new_nodes.append(node)
        else: #node needs to be split
            split_nodes_delimiter_helper(new_nodes, node, delimiter, text_type)
    return new_nodes
            
#splits a node containing another node based on given delimiter
#input: current list of split nodes, node to be split, delimiter str, text type Enum of inside node
#output: no return, mutatates new_nodes list with split nodes from old_node
def split_nodes_delimiter_helper(new_nodes, old_node, delimiter, text_type):
    delimiter_count = old_node.text.count(delimiter)
    if delimiter_count % 2 != 0:
        raise Exception(f"Invalid Markdown syntax: odd number of delimiter {delimiter}")
    split_value = old_node.text.split(delimiter)
    for i in range(delimiter_count + 1):
        if i % 2 == 0:  
            if split_value[i] != "":
                new_nodes.append(TextNode(split_value[i], TextType.NORMAL))
        else:
            new_nodes.append(TextNode(split_value[i], text_type))


#parses input text nodes into sectioned text and image nodes
#old_nodes: list of TextNodes
#returns list of TextNode(s) of either text or image type 
def split_nodes_image(old_nodes): ### !!! ADD SUPPORT FOR INPUTTING RAW MARKDOWN AS old_nodes
    if old_nodes is None or len(old_nodes) == 0:
        raise Exception("cannot split nodes without nodes")
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type.value != "normal":
            new_nodes.append(old_node)
        elif extract_markdown_images(old_node.text) is []:
            new_nodes.append(old_node)
        else:
            extracted_images = extract_markdown_images(old_node.text)
            split_text = [old_node.text]
            for i in range(len(extracted_images)):
                split_text = split_text[-1].split(f"![{extracted_images[i][0]}]({extracted_images[i][1]})", maxsplit=1)
                processed_node = split_text.pop(0)
                if processed_node != "":
                    new_nodes.append(TextNode(processed_node, TextType.NORMAL))
                new_nodes.append(TextNode(extracted_images[i][0], TextType.IMAGE, extracted_images[i][1]))
            processed_node = split_text.pop(0)
            if processed_node != "":
                new_nodes.append(TextNode(processed_node, TextType.NORMAL))
    return new_nodes

#parses input text nodes into sectioned text and link nodes
#old_nodes: list of TextNode of raw markdown text
#returns list of TextNode(s) of either text or link type 
def split_nodes_link(old_nodes):
    if old_nodes is None or len(old_nodes) == 0:
        raise Exception("cannot split nodes without nodes")
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type.value != "normal":
            new_nodes.append(old_node)
        elif extract_markdown_links(old_node.text) is []:
            new_nodes.append(old_node)
        else:
            extracted_links = extract_markdown_links(old_node.text)
            split_text = [old_node.text]
            for i in range(len(extracted_links)):
                split_text = split_text[-1].split(f"[{extracted_links[i][0]}]({extracted_links[i][1]})", maxsplit=1)
                processed_node = split_text.pop(0)
                if processed_node != "":
                    new_nodes.append(TextNode(processed_node, TextType.NORMAL))
                new_nodes.append(TextNode(extracted_links[i][0], TextType.LINK, extracted_links[i][1]))
            processed_node = split_text.pop(0)
            if processed_node != "":
                new_nodes.append(TextNode(processed_node, TextType.NORMAL))
    return new_nodes

#parses input text into appropriate type TextNode
#text: raw markdown text
#returns list of TextNode(s) of any type
def text_to_textnodes(text):
    node = TextNode(text, TextType.NORMAL)
    link_split = split_nodes_link([node])
    image_split = split_nodes_image(link_split)
    bold_split = split_nodes_delimiter(image_split, "**", TextType.BOLD)
    italic_split = split_nodes_delimiter(bold_split, "*", TextType.ITALIC)
    return split_nodes_delimiter(italic_split, "`", TextType.CODE)