"""
Docstring for december.markdown_blockquote_parser
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-17
                    Markdown Blockquote Parser
Given a string that includes a blockquote in Markdown, return the equivalent HTML string.

A blockquote in Markdown is any line that:

Starts with zero or more spaces
Followed by a greater-than sign (>)
Then, one or more spaces
And finally, the blockquote text.
Return the blockquote text surrounded by opening and closing HTML blockquote tags.

For example, given "> This is a quote", return <blockquote>This is a quote</blockquote>.
"""
def parse_blockquote(markdown):
    text = ""
    i = 0
    while i < len(markdown):
        if markdown[i] == " ":
            i+=1
        elif markdown[i] == ">":
            text = markdown[i + 1:].lstrip()
            break
    return f"<blockquote>{text}</blockquote>"
print(parse_blockquote("> This is a quote")      ) # should return "<blockquote>This is a quote</blockquote>".
print(parse_blockquote(" > This is also a quote")) # should return "<blockquote>This is also a quote</blockquote>".
print(parse_blockquote("  >    So  Is  This")    ) # should return "<blockquote>So  Is  This</blockquote>"