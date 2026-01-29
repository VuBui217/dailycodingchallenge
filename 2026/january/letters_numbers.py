"""
Docstring for 2026.january.letters_numbers
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-29
                    Letters-Numbers
Given a string containing only letters and numbers, return a new string where a hyphen (-) is inserted every time the string switches from a letter to a number, or a number to a letter.
"""
def separate_letters_and_numbers(s):
    output = []
    for i in range(len(s)):
        if i > 0 and s[i].isdigit() != s[i-1].isdigit():
            output.append("-")
        output.append(s[i])
    return "".join(output)

print(separate_letters_and_numbers("ABC123")    )  # should return "ABC-123".
print(separate_letters_and_numbers("Route66")   )  # should return "Route-66.
print(separate_letters_and_numbers("H3LL0W0RLD"))  # should return "H-3-LL-0-W-0-RLD".
print(separate_letters_and_numbers("a1b2c3d4")  )  # should return "a-1-b-2-c-3-d-4".