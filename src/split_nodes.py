from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if old_nodes is None or len(old_nodes) == 0:
        raise Exception("cannot split nodes without nodes")
    new_nodes = []
    for node in old_nodes:
        if node.text_type.value != "normal":
            new_nodes.append(node)
        elif node.text.count(delimiter) == 0:
            new_nodes.append(node)
        else:
            split_nodes_delimiter_helper(new_nodes, node, delimiter, text_type)
    return new_nodes
            

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