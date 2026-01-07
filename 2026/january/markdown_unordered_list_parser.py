"""
Docstring for 2026.january.markdown_unordered_list_parser
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-07
                    Markdown Unordered List Parser
Given the string of a valid unordered list in Markdown, return the equivalent HTML string.

An unordered list consists of one or more list items. A valid list item appears on its own line and:

Starts with a dash ("-"), followed by
At least one space, and then
The list item text.
The list is given as a single string with new lines separated by the newline character ("\n"). Do not include the newline characters in the item text.

Wrap each list item in HTML li tags, and the whole list of items in ul tags.

For example, given "- Item A\n- Item B", return "<ul><li>Item A</li><li>Item B</li></ul>".
"""
def parse_unordered_list(markdown):
    items_list = markdown.split("\n")
    # items_list = [item.lstrip("-").strip() for item in items_list]
    # res = ""
    # for item in items_list:
    #     res += "<li>" + item + "</li>"
    res = "".join(
        "<li>" + item.lstrip("-").strip() + "</li>"
        for item in items_list
    )
    return "<ul>"+ res + "</ul>"
print(parse_unordered_list("- Item A\n- Item B")                         ) # should return "<ul><li>Item A</li><li>Item B</li></ul>".
print(parse_unordered_list("-  JavaScript\n-  Python")                   ) # should return "<ul><li>JavaScript</li><li>Python</li></ul>".
print(parse_unordered_list("- 2 C Flour\n- 1/2 C Sugar\n- 1 Tsp Vanilla")) # should return "<ul><li>2 C Flour</li><li>1/2 C Sugar</li><li>1 Tsp Vanilla</li></ul>".
print(parse_unordered_list("- A-1\n- A-2\n- B-1")                        ) # should return "<ul><li>A-1</li><li>A-2</li><li>B-1</li></ul>".