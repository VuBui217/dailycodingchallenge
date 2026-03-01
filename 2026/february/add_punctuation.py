"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-28
Add Punctuation
Given a string of sentences with missing periods, add a period (".") in the following places:

Before each space that comes immediately before an uppercase letter
And at the end of the string
Return the resulting string.
"""
def add_punctuation(sentences):
    output = []
    n = len(sentences)
    for i in range(len(sentences)):
        if (sentences[i] == " " and i + 1 < n and sentences[i + 1].isupper()):
            output.append(".")
        output.append(sentences[i])
    output.append(".")
    return "".join(output)

print(add_punctuation("Hello world"))                                          # should return "Hello world."
print(add_punctuation("Hello world It's nice today"))                          # should return "Hello world. It's nice today."
print(add_punctuation("JavaScript is great Sometimes"))                        # should return "JavaScript is great. Sometimes."
print(add_punctuation("A b c D e F g h I J k L m n o P Q r S t U v w X Y Z"))  # should return "A b c. D e. F g h. I. J k. L m n o. P. Q r. S t. U v w. X. Y. Z."
print(add_punctuation("Wait.. For it"))                                        # should return "Wait... For it."