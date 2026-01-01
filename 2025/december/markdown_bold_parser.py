"""
Docstring for december.markdown_bold_parser
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-10

                                Markdown Bold Parser
Given a string that may include some bold text in Markdown, return the equivalent HTML string.

Bold text in Markdown is any text that starts and ends with two asterisks (**) or two underscores (__).
There cannot be any spaces between the text and the asterisks or underscores, but there can be spaces in the text itself.
Convert all bold occurrences to HTML b tags and return the string.
For example, given "**This is bold**", return "<b>This is bold</b>".
"""
def parse_bold(markdown):
    import re
    pattern = r'(\*\*|__)(\S(?:.*?\S)?)\1'
    return re.sub(pattern, r'<b>\2</b>', markdown)

print(parse_bold("**This is bold**")                                        )  # should return "<b>This is bold</b>".
print(parse_bold("__This is also bold__")                                   )  # should return "<b>This is also bold</b>".
print(parse_bold("**This is not bold **")                                   )  # should return "**This is not bold **".
print(parse_bold("__ This is also not bold__")                              )  # should return "__ This is also not bold__".
print(parse_bold("The **quick** brown fox __jumps__ over the **lazy** dog."))  # should return "The <b>quick</b> brown fox <b>jumps</b> over the <b>lazy</b> dog."