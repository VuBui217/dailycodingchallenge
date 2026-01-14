"""
Docstring for 2026.january.markdown_link_parser
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-14
                        Markdown Link Parser
Given the string of a link in Markdown, return the equivalent HTML string.

A Markdown image has the following format: "[link_text](link_url)". Return the string of the HTML a tag with the href set to the link_url and the link_text as the tag content.

For example, given "[freeCodeCamp](https://freecodecamp.org/)" return '<a href="https://freecodecamp.org/">freeCodeCamp</a>';

Note: The console may not display HTML tags in strings when logging messages — check the browser console to see logs with tags included.
"""
def parse_link(markdown):
    text_start = markdown.index("[")
    text_end = markdown.index("]")
    url_start = markdown.index("(")
    url_end = markdown.index(")")

    link_text = markdown[text_start + 1 : text_end]
    link_url = markdown[url_start + 1 : url_end]

    return f'<a href="{link_url}">{link_text}</a>'


print(parse_link("[freeCodeCamp](https://freecodecamp.org/)")) # should return '<a href="https://freecodecamp.org/">freeCodeCamp</a>'.
print(parse_link("[Donate to our charity.](https://www.freecodecamp.org/donate/)")) # should return '<a href="https://www.freecodecamp.org/donate/">Donate to our charity.</a>'.
print(parse_link("[Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.](https://github.com/freeCodeCamp/freeCodeCamp/)")) # should return '<a href="https://github.com/freeCodeCamp/freeCodeCamp/">Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.</a>'.