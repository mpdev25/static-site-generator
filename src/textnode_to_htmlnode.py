import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown text, unmatched delimiter")

        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 ==0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes 

def extract_markdown_images(text):
    patern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(patern, text)
    return matches

def extract_markdown_links(text):
    patern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(patern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        images = extract_markdown_images(original_text)
        if not images:
            new_nodes.append(node)
            continue
        
        
        for alt, url in images:
            sections = original_text.split(f"![{alt}]({url})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    alt,
                    TextType.IMAGE,
                    url,
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
        
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        links = extract_markdown_links(original_text)
        if not links:
            new_nodes.append(node)
            continue
        
        for label, url in links:
            sections = original_text.split(f"[{label}]({url})", 1)
            if len(sections) !=2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(label, TextType.LINK, url))
            original_text = sections[1]
        if original_text != "":
        
            new_nodes.append(TextNode(original_text, TextType.TEXT))
           
    return new_nodes

def text_to_textnodes(text):
    
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_image(nodes)

    nodes = split_nodes_link(nodes)
    
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    
    
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    

    return nodes