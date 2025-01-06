import re

#extracts alt text and url for any images in inputted markdown text
#text: string of raw markdown text
#returns list of tuples (alt text, url)
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

#extracts alt text and url for any links in inputted markdown text
#text: string of raw markdown text
#retruns list of tuples (alt text, url)
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)