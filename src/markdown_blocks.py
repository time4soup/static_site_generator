import re

# splits raw markdown into blocks of one type (based on empty line "" btwn blocks)
# input: raw markdown (string)
# output: list of markdown block (list of strings)
def markdown_to_blocks(markdown):
    clean_markdown = markdown.strip("\n")
    lines = clean_markdown.split("\n")
    strip_lines = list(map(lambda x: x.strip(), lines))
    block_strings = []
    line_to_add = ""
    for strip_line in strip_lines:
        if strip_line == "":
            if line_to_add != "":
                block_strings.append(line_to_add.rstrip("\n"))
            line_to_add = ""
        else:
            line_to_add = line_to_add + strip_line + "\n"
    if line_to_add != "":
        block_strings.append(line_to_add.rstrip("\n"))
    return block_strings

# finds which type a given block of markdown fits into (based on markdown syntax)
# input: block of markdown (string)
# output: name of markdown type (string)
def block_to_block_type(block):
    split_block = block.split("\n")
    if check_regex(r"\#{1,6} .*?", block):
        return "heading"
    if check_regex(r"```.*?```", block) or (check_regex(r"```.*?", split_block[0]) and check_regex(r".*?```", split_block[-1])):
        return "code"
    if check_regex(r">.*?", split_block):
        return "quote"
    if check_regex(r"[\*\-] .*?", split_block):
        return "unordered list"
    if check_regex(r"\d+\. .*?", split_block) \
        and [int(line[0]) for line in split_block] == [num for num in range(1, len(split_block) + 1)]:
        return "ordered list"
    else:
        return "paragraph"

#checks if input obj matches regex provided
#input: test object (string or list of strings), output: bool
def check_regex(regex, obj):
    if isinstance(obj, str):
        if re.fullmatch(regex, obj):
            return True
        return False
    if isinstance(obj, list):
        if len(list(filter(lambda x: re.fullmatch(regex, x), obj))) == len(obj):
            return True
        return False
    raise Exception(f"check_regex only accepts str or list not {type(obj)}")
    