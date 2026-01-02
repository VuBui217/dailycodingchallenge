"""
Docstring for 2025.december.markdown_italic_parser
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-31
                        Markdown Italic Parser
Given a string that may include some italic text in Markdown, return the equivalent HTML string.

Italic text in Markdown is any text that starts and ends with a single asterisk (*) or a single underscore (_).
There cannot be any spaces between the text and the asterisk or underscore, but there can be spaces in the text itself.
Convert all italic occurrences to HTML i tags and return the string.
For example, given "*This is italic*", return "<i>This is italic</i>".
"""
def parse_italics(markdown):
    output = []
    n = len(markdown)
    i = 0
    while i < n:
        if markdown[i] in ("*", "_"):
            marker = markdown[i]
            start = i
            i += 1
            while i < n and markdown[i] != marker:
                i += 1
            end = i
            if markdown[start + 1] != " " and markdown[end - 1] != " ":
                text = markdown[start + 1 : end]
                output.append(f"<i>{text}</i>")
            else:
                output.append(markdown[start: end + 1])
            i += 1
        else:
            output.append(markdown[i])
            i += 1
    return "".join(output)

print(parse_italics("*This is italic*")                                 ) # should return "<i>This is italic</i>".
print(parse_italics("_This is also italic_")                            ) # should return "<i>This is also italic</i>".
print(parse_italics("*This is not italic *")                            ) # should return "*This is not italic *".
print(parse_italics("_ This is also not italic_")                       ) # should return "_ This is also not italic_".
print(parse_italics("The *quick* brown fox _jumps_ over the *lazy* dog.")) # should return "The <i>quick</i> brown fox <i>jumps</i> over the <i>lazy</i> dog.".