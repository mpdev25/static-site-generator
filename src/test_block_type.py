import unittest
import re
from textnode import TextNode, TextType
from block_type import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks
class TestBlockType(unittest.TestCase):
    def test_block_to_block_type_paragraph(self):
        markdown = """
This is a paragraph
This is a second paragraph
"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(
            block_type,
            
            BlockType.PARAGRAPH
            
        )

    def test_block_to_block_type_quote(self):
        markdown = """> This is a quote"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(
            block_type,
            BlockType.QUOTE    
        )

    def test_block_to_block_type_code(self):
        markdown = """```This is code```"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(
            block_type,
            BlockType.CODE    
        )

    def test_block_to_block_type_heading(self):
        markdown = """### This is a heading"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(
            block_type,
            BlockType.HEADING    
        )

    def test_block_to_block_type_unordered_list(self):
        markdown = """- This is a list
- With two entries"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(
            block_type,
            BlockType.UNORDERED_LIST    
        )

    def test_block_to_block_type_ordered_list(self):
        markdown = """1. This is a list
2. It is in order"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(
            block_type,
            BlockType.ORDERED_LIST    
        )