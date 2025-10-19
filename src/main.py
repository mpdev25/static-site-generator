import os
import shutil

from textnode import TextType
from textnode import TextNode
from copystatic import copy_static
from generate_page import generate_page
def main():
    dest_path = "public"
    for item in os.listdir(dest_path):
        item_path = os.path.join(dest_path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)  
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)

    static = "static"
    public = "public"
    copy_static(static, public)
    from_paths = [
        "content/index.md",
        "content/blog/majesty/index.md",
        "content/blog/tom/index.md",
        "content/contact/index.md"
    ]
 
    template_path = "template.html"
   
    for from_path in from_paths:
        
        
        generate_page(from_path, template_path, dest_path)
    
    


if __name__ == "__main__":
    main()

    

    

