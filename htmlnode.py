class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Child class did not override to_html function")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        str = ""
        for key, value in self.props.items():
            str = str + (f" {key}='{value}'")
        return str
    
    def __repr__(self):
        print(f"tag: {self.tag}")
        print(f"value: {self.value}")
        print(f"children: {self.children}")
        print(f"props: {self.props}")
    
    def __eq__(self, other):
        return self.tag == other.tag \
        and self.value == other.value \
        and self.children == other.children \
        and self.props == other.props


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("leaf node without value")
        if self.tag is None:
            return self.value
        props_html = ""
        if self.props is not None:
            for key, value in self.props.items():
                props_html = f" {key}=\"{value}\""
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent has no tag")
        if self.children is None:
            raise ValueError("Parent has no children")
        props_html = ""
        if self.props is not None:
            for key, value in self.props.items():
                props_html = f" {key}=\"{value}\""
        html_string = f"<{self.tag}{props_html}>"
        for child in self.children:
            html_string = html_string + child.to_html()
        return html_string + f"</{self.tag}>"