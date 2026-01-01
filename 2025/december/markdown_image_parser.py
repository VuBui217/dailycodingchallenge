"""
Docstring for december.markdown_image_parser
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-24
                            Markdown Image Parser
Given a string of an image in Markdown, return the equivalent HTML string.

A Markdown image has the following format: "![alt text](image_url)". Where:

alt text is the description of the image (the alt attribute value).
image_url is the source URL of the image (the src attribute value).
Return a string of the HTML img tag with the src set to the image URL and the alt set to the alt text.

For example, given "![Cute cat](cat.png)" return '<img src="cat.png" alt="Cute cat">';

Make sure the tag, order of attributes, spacing, and quote usage is the same as above.  
"""
def parse_image(markdown):
    alt = markdown[markdown.index("[") + 1 : markdown.index("]")]
    url = markdown[markdown.index("(") + 1 : markdown.index(")")]
    return f'<img src="{url}" alt="{alt}">'

print(parse_image("![Cute cat](cat.png)")                                        ) # should return '<img src="cat.png" alt="Cute cat">'.
print(parse_image("![Rocket Ship](https://freecodecamp.org/cdn/rocket-ship.jpg)")) # should return '<img src="https://freecodecamp.org/cdn/rocket-ship.jpg" alt="Rocket Ship">'.
print(parse_image("![Cute cats!](https://freecodecamp.org/cats.jpeg)")           ) # should return '<img src="https://freecodecamp.org/cats.jpeg" alt="Cute cats!">'