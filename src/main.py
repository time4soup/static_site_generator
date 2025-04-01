from copy_file_tree import copy_file_tree
from generate_page import generate_pages_recursive

def main():
    static = r"./static"
    public = r"./public"
    copy_file_tree(static, public)

    generate_pages_recursive(r"content", r"template.html", r"public")
main()
