#html node represents a tag in html (inline or block)
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # no tag == raw text
        self.value = value # nodes must have either value or children 
        self.children = children 
        self.props = props 
    
    def to_html(self):
        raise NotImplementedError("Child class did not override to_html function")
    
    # returns props key-value pairs in html format
    # eg. "href": "http://website.com" -> href="http://website.com"
    def props_to_html(self):
        if self.props is None:
            return ""
        str = ""
        for key, value in self.props.items():
            str = str + (f" {key}='{value}'")
        return str
    
    def __repr__(self):
        return f"""
LeafNode:
tag: {self.tag}
value: 
{self.value}
children:
{self.children}
props: {self.props}
"""
    
    def __eq__(self, other):
        return self.tag == other.tag \
        and self.value == other.value \
        and self.children == other.children \
        and self.props == other.props

# html object with no nested nodes inside
# has no children
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props) #leaf nodes have no children
    
    # returns leaf node as html string with tags
    def to_html(self):
        if self.value is None:
            raise ValueError("leaf node without value")
        if self.tag is None:
            return self.value
        props_html = ""
        if self.props is not None:
            for key, value in self.props.items():
                props_html = f"{props_html} {key}=\"{value}\""
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"""
LeafNode:
tag: {self.tag}
value: 
{self.value}
props: {self.props}
"""

# has no value but has children
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
        return f"""
ParentNode:
tag: {self.tag}
children: 
{self.children}
props: {self.props}
"""
    
    # outputs html string for parent node and all children recursively
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