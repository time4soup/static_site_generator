from enum import Enum
from htmlnode import LeafNode

# textnode represents one inline elements (either html or markdown)
# does not support children / nested elements
class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other):
        return self.text == other.text \
        and self.text_type == other.text_type \
        and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def text_node_to_html_node(self):
        if not isinstance(type(self), type(TextNode)):
            raise Exception(f"text_type must be TextType, not {self.text_type}")
        match self.text_type.value:
            case "normal":
                return LeafNode(None, self.text)
            case "bold":
                return LeafNode("b", self.text)
            case "italic":
                return LeafNode("i", self.text)
            case "code":
                return LeafNode("code", self.text)
            case "link":
                return LeafNode("a", self.text, {"href": self.url})
            case "image":
                return LeafNode("img", "", {"src": self.url, "alt": self.text})
            case _:
                raise Exception("not valid TextType type")

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"