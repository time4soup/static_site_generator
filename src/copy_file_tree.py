import os
import shutil

from textnode import TextNode
from markdown_to_html import markdown_to_html_node

# deep copies entire file tree from src to dest
# deletes any existing files in dest
def copy_file_tree(src, dest):
    if not os.path.exists(src):
        raise ValueError(f"{src} does not exist")
    if not os.path.exists(dest):
        raise ValueError(f"{dest} does not exist")
    print("directories validated")

    shutil.rmtree(dest)
    os.mkdir(dest)
    print(f"{dest} emptied")
    
    tree = get_files(src)
    print(f"files to copy: {tree}")

    for item in tree:
        copy_item(item, src, dest)
        print(f"item copied: {item}")

# returns list of files and subfiles in dir
def get_files(dir):
    entries = os.listdir(dir)
    tree = []
    for entry in entries:
        entry = os.path.join(dir, entry)
        if os.path.isfile(entry):
            tree.append(entry)
        else:
            tree.extend(get_files(entry))
    return tree
        
def copy_item(item, src, dest): 
    common_path = item.removeprefix(src).lstrip("/") #common part of the path relative to src/dest dirs
    split_common_path = common_path.split("/") 
    while len(split_common_path) > 1:
        dir = split_common_path.pop(0)
        dest = os.path.join(dest, dir)
        if not os.path.exists(dest):
            os.mkdir(dest)
    shutil.copy(item, dest)

def write_item(item, contents):
    split_path = item.lstrip("/").split("/") 
    dest = ""
    while len(split_path) > 1:
        dir = split_path.pop(0)
        dest = os.path.join(dest, dir)
        if not os.path.exists(dest):
            os.mkdir(dest)
    
    dir = split_path.pop(0)
    dest = os.path.join(dest, dir)
    with open(dest, "w") as write_file:
        write_file.write(contents)
    