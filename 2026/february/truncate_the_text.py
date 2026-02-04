"""
Docstring for 2026.february.truncate_the_text
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-04
                    Truncate the Text
Given a string, return it as-is if it's 20 characters or shorter. If it's longer than 20 characters, truncate it to the first 17 characters and append "..." to the end of it (so it's 20 characters total) and return the result.
"""
def truncate_text(text):
    if len(text) > 20:
        return text[:17] + "..."
    return text 

print(truncate_text("Hello, world!")                    )  # should return "Hello, world!".
print(truncate_text("This string should get truncated."))  # should return "This string shoul...".
print(truncate_text("Exactly twenty chars")             )  # should return "Exactly twenty chars".
print(truncate_text(".....................")            )  # should return "....................".