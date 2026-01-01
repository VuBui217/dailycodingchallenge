"""
Docstring for december.markdown_ordered_list_item_converter
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-03

                            Markdown Ordered List Item Converter
Given a string representing an ordered list item in Markdown, return the equivalent HTML string.

A valid ordered list item in Markdown must:

Start with zero or more spaces, followed by
A number (1 or greater) and a period (.), followed by
At least one space, and then
The list item text.
If the string doesn't have the exact format above, return "Invalid format". Otherwise, wrap the list item text in li tags and return the string.

For example, given "1. My item", return  "<li>My item</li>"
"""
def convert_list_item(markdown):
    line = markdown.strip()

    i = 0
    while i < len(line) and line[i].isdigit():
        i += 1
    # Must start with at least one number
    if i == 0:
        return "Invalid format"
    # Expect a period
    if i >= len(line) or line[i] != ".":
        return "Invalid format"
    i = i + 1
    # Expect at least a space
    if i >= len(line) or line[i] != " ":
        return "Invalid format"

    # Extract the text
    text = line[i:].strip()   

    return f"<li>{text}</li>"

convert_list_item("1. My item")         # should return "<li>My item</li>".
convert_list_item(" 1.  Another item")  # should return "<li>Another item</li>".
convert_list_item("1 . invalid item")   # should return "Invalid format".
convert_list_item("2. list item text")  # should return "<li>list item text</li>".
convert_list_item(". invalid again")    # should return "Invalid format".
convert_list_item("A. last invalid")    # should return "Invalid format".