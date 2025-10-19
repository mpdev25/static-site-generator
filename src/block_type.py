import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = ("paragraph")
    HEADING = ("heading")
    CODE = ("code")
    QUOTE = ("quote")
    UNORDERED_LIST = ("unordered_list")
    ORDERED_LIST = ("ordered_list")

def block_to_block_type(markdown):

    prefixes = ('# ', '## ', '### ', '#### ', '##### ', '###### ')
    if markdown.startswith(prefixes):
        return BlockType.HEADING

    if markdown.startswith('```') and markdown.endswith('```'):
        return BlockType.CODE

    if markdown.startswith('>'):
        return BlockType.QUOTE

    if markdown.startswith('- '):
        return BlockType.UNORDERED_LIST

    if re.match(r'^\d+\. ', markdown):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH