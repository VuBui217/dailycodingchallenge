"""
Docstring for december.camel_to_snake
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-02

                                Camel to Snake
Given a string in camel case, return the snake case version of the string using the following rules:

The input string will contain only letters (A-Z and a-z) and will always start with a lowercase letter.
Every uppercase letter in the camel case string starts a new word.
Convert all letters to lowercase.
Separate words with an underscore (_).
"""
def to_snake(camel):
    output = []

    for ch in camel:
        if ch.isupper():
            output.append("_")
            output.append(ch.lower())
        else:
            output.append(ch)
    return "".join(output)

print(to_snake("helloWorld")                 ) # should return "hello_world".
print(to_snake("myVariableName")             ) # should return "my_variable_name".
print(to_snake("freecodecampDailyChallenges")) # should return "freecodecamp_daily_challenges".