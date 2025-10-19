import  re
from markdown_to_blocks import markdown_to_blocks
from block_type import BlockType, block_to_block_type
from textnode_to_htmlnode import text_to_textnodes
from htmlnode import HTMLNode, ParentNode, LeafNode, text_node_to_html_node
from textnode import TextNode
def markdown_to_html_node(markdown):
    
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        ready_block = block_to_block_type(block)
        if ready_block == BlockType.PARAGRAPH:
            content = "\n".join(ln.strip() for ln in block.strip().split("\n"))
            content = " ".join(content.split())
            children = text_to_children(content)
            html_nodes.append(ParentNode(tag="p", children=children))
            
        elif ready_block == BlockType.HEADING:
           
            content = block.lstrip()
            if not content.startswith("#"):
                raise ValueError("Incorrectly formatted heading.")
            level = 0
            for char in content:
                if char == '#':
                    level +=1
                else:
                    break
            if level < 1 or level > 6:
                    raise ValueError("Incorrectly formatted heading.")
            if len(content) <= level or content[level] != " ":
                    raise ValueError("Incorrectly formatted heading.")
            text = content[level + 1 :].strip()
            children = text_to_children(text)
            html_nodes.append(ParentNode(tag=f"h{level}", children=children))
            
        elif ready_block == BlockType.CODE:
            inner = extract_fenced_code(block)
            code_child = LeafNode(None, inner)
            code_node = ParentNode("code", [code_child])
            html_nodes.append(ParentNode("pre", [code_node]))

        elif ready_block == BlockType.QUOTE:
            content = strip_markers(block)
            children = text_to_children(content)
            html_nodes.append(ParentNode(tag="blockquote", children=children))
            
        elif ready_block == BlockType.UNORDERED_LIST:
            items = list_split(block, ordered=False)
            children = [ParentNode("li", text_to_children(it)) for it in items]
            node = ParentNode("ul", children)
            html_nodes.append(node)
        elif ready_block == BlockType.ORDERED_LIST:
            items = list_split(block, ordered=True)
            children = [ParentNode("li", text_to_children(it)) for it in items]
            node = ParentNode("ol", children)
            html_nodes.append(node)
    parent_node = parent_node_creator(html_nodes)
    return ParentNode("div", html_nodes)

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    return [text_node_to_html_node(tn) for tn in textnodes]

def parent_node_creator(html_nodes):
    return ParentNode("div", html_nodes)

def strip_markers(block):
    pattern = re.compile(r"^(>|\s*[-*+]|\s*\d+\.)\s*")
    cleaned_lines = []
    for line in block.strip().split('\n'):
        
        cleaned_lines.append(pattern.sub('', line))
    return '\n'.join(cleaned_lines)

def extract_fenced_code(block):
    
    lines = block.strip().split("\n")
    if not lines:
        return ""
    first_line = lines[0].strip()
    last_line = lines[-1].strip()
    if first_line.startswith("```") and last_line.endswith("```"):
        inner = lines[1:-1]
        return "\n".join(inner) + "\n"
        
    return block

def list_split(block, ordered=False):
    lines = [ln for ln in block.strip().split("\n") if ln.strip()]
    if ordered:
        pat = re.compile(r"^\s*\d+\.\s*")
    else:
        pat = re.compile(r"^\s*[-*+]\s*")

    return [pat.sub("", ln) for ln in lines]

def to_html(node):
    return node.to_html()