"""
Docstring for december.screaming_snake_case
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-28
                            SCREAMING_SNAKE_CASE
Given a string representing a variable name, return the variable name converted to SCREAMING_SNAKE_CASE.

The given variable names will be written in one of the following formats:

camelCase
PascalCase
snake_case
kebab-case
In the above formats, words are separated by an underscore (_), a hyphen (-), or a new word starts with a capital letter.

To convert to SCREAMING_SNAKE_CASE:

Make all letters uppercase
Separate words with an underscore (_)
"""
def to_screaming_snake_case(variable_name):
    output = []
    for i in range(len(variable_name)):
        ch = variable_name[i]
        if ch == "_" or ch == "-":
            output.append("_")
            continue
        if ch.isupper() and i > 0:
            output.append("_")
        output.append(ch.upper())
    return "".join(output)
print(to_screaming_snake_case("userEmail")   ) # should return "USER_EMAIL".
print(to_screaming_snake_case("UserPassword")) # should return "USER_PASSWORD".
print(to_screaming_snake_case("user_id")     ) # should return "USER_ID".
print(to_screaming_snake_case("user-address")) # should return "USER_ADDRESS".
print(to_screaming_snake_case("username")    ) # should return "USERNAME".
