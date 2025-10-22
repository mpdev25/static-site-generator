import os
import shutil

from textnode import TextType

def copy_static(static, docs):
    
    if os.path.exists(docs):
        try:
            shutil.rmtree(docs)
        except:
            print(f"Error: could not delete '{docs}'.")
    try:
        os.mkdir(docs)
    except:
        print(f"Error: could not recreate '{docs}'.")
    
    if not os.path.exists(docs):
        os.makedirs(docs)
    for item in os.listdir(static):
        static_path = os.path.join(static, item)
        docs_path = os.path.join(docs, item)

        if os.path.isfile(static_path):
            shutil.copy2(static_path, docs_path)
        elif os.path.isdir(static_path):
            copy_static(static_path, docs_path)