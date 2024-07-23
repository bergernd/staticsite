


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

block = '''# This is a heading
	
This is a paragraph of text. It has some **bold** and *italic* words inside of it.
	
* This is the first list item in a list block
* This is a list item
* This is another list item'''

print(markdown_to_blocks1(block))
