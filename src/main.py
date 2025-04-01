import sys

from copy_file_tree import copy_file_tree
from generate_page import generate_pages_recursive

def main():
    copy_src_path = r"./static"
    copy_dest_path = r"./docs"
    copy_file_tree(copy_src_path, copy_dest_path)

    root_dir = "/"
    if len(sys.argv) > 1:
        root_dir = sys.argv[1]
    generate_pages_recursive(r"content", r"template.html", r"docs", root_dir)
main()
