import re
import os.path

from markdown_to_html import markdown_to_html_node
from htmlnode import ParentNode
from copy_file_tree import write_item, get_files

# takes markdown string and returns first h1 instance
def extract_title(markdown):
    match = re.search(r"(?<!#)# .+", markdown)
    if match == None:
        raise ValueError("markdown does not contain title")
    return match.group().lstrip("# ")

# takes markdown from from_path and uses template at template_path to generate and store html file at dest_path
def generate_page(from_path, template_path, dest_path, root_dir):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as from_file:
        markdown = from_file.read()
    with open(template_path, "r") as template_file:
        template = template_file.read()
    
    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Content }}", html)
    template = template.replace("{{ Title }}", title)
    template = template.replace("href=\"/", f"href=\"{root_dir}")
    template = template.replace("src=\"/", f"src=\"{root_dir}")

    write_item(dest_path, template)

# finds all markdown files (.md) in given dir_path_content and creates html file in same directory
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, root_dir):
    files = get_files(dir_path_content)
    for file in files:
        if not file.split(".")[1] == "md":
            continue
        base_file_name = file.removeprefix(dir_path_content).rstrip("md")
        file_dest = dest_dir_path + base_file_name + "html"
        generate_page(file, template_path, file_dest, root_dir)