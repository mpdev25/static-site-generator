import os
import shutil
import sys
from textnode import TextType
from textnode import TextNode
from copystatic import copy_static

#from generate_page import generate_page
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
def main():
    base_path = "/"
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    print(f"The basepath is: {base_path}")
    dest_path = "docs"
  

    static = "static"
    docs = "docs"
    copy_static(static, docs)
    from_paths = [
        "content/index.md",
        "content/blog/glorfindel/index.md",
        "content/blog/majesty/index.md",
        "content/blog/tom/index.md",
        "content/contact/index.md"
    ]
 
    template_path = "template.html"

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
        template_with_href = template_adjusted.replace('href="/', f'href="{base_path}')
        template_with_content = template_with_href.replace('src="/', f'src="{base_path}')
        stripped_path = from_path.replace("content/", "", 1)
        root, _ = os.path.splitext(stripped_path)
        html_path = root + ".html"
        dest_path = os.path.join("docs", html_path)
        dest_dir = os.path.dirname(dest_path)
        if dest_dir and not os.path.exists(dest_dir):
            os.makedirs(dest_dir, exist_ok=True)

        try:
            with open(dest_path, 'w') as f:
                f.write(template_with_content)
        except Exception as e:
            print(f"An error has occurred while writing the page: {e}")
            return
   
    for from_path in from_paths:
        
        
        generate_page(from_path, template_path, dest_path=base_path)
    
    
    


if __name__ == "__main__":
    main()

    

    

