from textnode import TextNode

def main():
    node = TextNode("text", "normal", None)
    node2 = TextNode("text", "normal")
    print(node)
    print(node == node2)

main()