from enum import Enum

class TextType(Enum):
    TEXT = ('text')
    BOLD = ('bold', '**Bold text**', '<b>', '</b>')
    ITALIC = ('italic', '_Italic text_', '<i>', '</i>')
    CODE = ('code', '`Code text`', '<code>', '</code>')
    LINK = ('links', '[anchor text](url)', '<a href="">link</a>')
    IMAGE = ('image', '![alt text](url)', '<img src=""alt="" />')
    
    
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
            )
              

    def __repr__(self):
        return f"'TextNode('{self.text}, {self.text_type}, {self.url}')'"

        