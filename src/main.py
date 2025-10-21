import os
import shutil

from textnode import TextType
from textnode import TextNode
from copystatic import copy_static
from generate_page import generate_page
def main():
    dest_path = "public"
  

    static = "static"
    public = "public"
    copy_static(static, public)
    from_paths = [
        "content/index.md",
        "content/blog/glorfindel/index.md",
        "content/blog/majesty/index.md",
        "content/blog/tom/index.md",
        "content/contact/index.md"
    ]
 
    template_path = "template.html"
   
    for from_path in from_paths:
        
        
        generate_page(from_path, template_path, dest_path)
    
    


if __name__ == "__main__":
    main()

    

    

