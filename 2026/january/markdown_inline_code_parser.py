"""
Docstring for 2026.january.markdown_inline_code_parser
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-21
                    Markdown Inline Code Parser
Given a string of Markdown that includes one or more inline code blocks, return the equivalent HTML string.

Inline code blocks in Markdown use a single backtick (`) at the start and end of the code block text.

Return the given string with all code blocks converted to HTML code tags.

For example, given the string "Use `let` to declare the variable.", return "Use <code>let</code> to declare the variable.".
"""
def parse_inline_code(markdown):
    output = []
    is_open = True
    for ch in markdown:
        if ch == "`" and is_open:
            output.append("<code>")
            is_open = False
        elif ch == "`" and not is_open:
            output.append("</code>")
            is_open = True
        else:
            output.append(ch)
    return "".join(output)

print(parse_inline_code("Use `let` to declare the variable.")         )    # should return "Use <code>let</code> to declare the variable.".
print(parse_inline_code("Use `let` or `const` to declare a variable."))    # should return "Use <code>let</code> or <code>const</code> to declare a variable.".
print(parse_inline_code("Run `npm install` then `npm start`.")        )    # should return "Run <code>npm install</code> then <code>npm start</code>.".