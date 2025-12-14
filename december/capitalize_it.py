"""
Docstring for december.capitalize_it
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-14
                        Capitalize It
Given a string title, return a new string formatted in title case using the following rules:

Capitalize the first letter of each word.
Make all other letters in each word lowercase.
Words are always separated by a single space.
"""
def title_case(title):
    return " ".join([word.lower().capitalize() for word in title.split()])

print(title_case("hello world")                )  # should return "Hello World".
print(title_case("the quick brown fox")        )  # should return "The Quick Brown Fox".
print(title_case("JAVASCRIPT AND PYTHON")      )  # should return "Javascript And Python".
print(title_case("AvOcAdO tOAst fOr brEAkfAst"))  # should return "Avocado Toast For Breakfast"