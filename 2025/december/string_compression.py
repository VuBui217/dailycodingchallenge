"""
Docstring for december.string_compression
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-07

                                        String Compression
Given a string sentence, return a compressed version of the sentence where consecutive duplicate words are replaced by the word followed with the number of times it repeats in parentheses.

Only consecutive duplicates are compressed.
Words are separated by single spaces.
For example, given "yes yes yes please", return "yes(3) please".
"""
def compress_string(sentence):
    lst = sentence.split(" ")
    res = []
    count = 1
    for i in range(1, len(lst) + 1):
        
        if i < len(lst) and lst[i] == lst[i - 1]:
            count += 1
        else:
            if count == 1:
                res.append(lst[i-1])
            else:
                res.append(f"{lst[i-1]}({count})")
            count = 1

    return " ".join(res)
print(compress_string("yes yes yes please")                                         )     # should return "yes(3) please".
print(compress_string("I have have have apples")                                    )     # should return "I have(3) apples".
print(compress_string("one one three and to the the the the")                       )     # should return "one(2) three and to the(4)".
print(compress_string("route route route route route route tee tee tee tee tee tee"))     # should return "route(6) tee(6)".
print(compress_string(""))