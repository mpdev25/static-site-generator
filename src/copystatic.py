import os
import shutil

from textnode import TextType

def copy_static(static, public):
    
    if os.path.exists(public):
        try:
            shutil.rmtree(public)
        except:
            print(f"Error: could not delete '{public}'.")
    try:
        os.mkdir(public)
    except:
        print(f"Error: could not recreate '{public}'.")
    
    if not os.path.exists(public):
        os.makedirs(public)
    for item in os.listdir(static):
        static_path = os.path.join(static, item)
        public_path = os.path.join(public, item)

        if os.path.isfile(static_path):
            shutil.copy2(static_path, public_path)
        elif os.path.isdir(static_path):
            copy_static(static_path, public_path)