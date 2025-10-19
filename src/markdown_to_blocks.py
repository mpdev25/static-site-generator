import re
from textnode import TextNode, TextType

def markdown_to_blocks(markdown):
    
    unprepared_blocks = markdown.split("\n\n")
    blocks = []
    for block in unprepared_blocks:
        
        ready_block = block.strip()
        if ready_block:
         
            blocks.append(ready_block)
    
    return blocks