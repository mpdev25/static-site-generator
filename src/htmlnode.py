from textnode import TextType, TextNode

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __to_html__(self):
        raise NotImplementedError

    def __props_to_html__(self):
        
        if self.props is None:
            return ""
        attribute_strings = ""
        for key, value in self.props.items():
            attribute_strings += f' {key}="{value}"'
        return " ".join(attribute_strings)

    def __repr__(self):
        return f"HTMLNode(tag='{self.tag}', value='{self.value}', children='{self.children}', props='{self.props}')"

    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
            return True
        else:
            return False


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        
        super().__init__(tag, value, children=None, props=props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf nodes require a value.")
        if self.tag is None:
            return self.value
        if self.props:
            prop_str = ""
            for key, value in self.props.items():
                prop_str += f' {key}="{value}"'
            return f"<{self.tag}{prop_str}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

    
       

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        
        super().__init__(tag, None, children, props)

    def to_html(self):
        
        if self.tag is None:
            raise ValueError("Parent nodes require a tag.")
        if self.children is None:
            raise ValueError("Parent nodes require children.")
        children_html = ""
       
        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}{self.__props_to_html__()}>{children_html}</{self.tag}>"


def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception(f"{text_node} is not a valid text type.")
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

     
      
    