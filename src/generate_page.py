import os
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    try:
        with open(from_path) as file:
            original_markdown = file.read()
    except FileNotFoundError:
        print(f"Error: The file {from_path} was not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return 
    try:
        with open(template_path) as file:
            template = file.read()
    except FileNotFoundError:
        print(f"Error: The file {template_path} was not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return
    
    prepared_markdown = markdown_to_html_node(original_markdown)
    content = prepared_markdown.to_html()
    title = extract_title(original_markdown)
    template_with_title = template.replace("{{ Title }}", title)
    template_adjusted = template_with_title.replace("{{ Content }}", content)
    template_with_href = template_adjusted.replace('href="/"', f'href="{base_path}"')
    template_with_content = template_with_href.replace('src="/"', f'src="{base_path}"')
    stripped_path = from_path.replace("content/", "", 1)
    root, _ = os.path.splitext(stripped_path)
    html_path = root + ".html"
    dest_path = os.path.join("public", html_path)
    dest_dir = os.path.dirname(dest_path)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)

    try:
        with open(dest_path, 'w') as f:
            f.write(template_with_content)
    except Exception as e:
        print(f"An error has occurred while writing the page: {e}")
        return