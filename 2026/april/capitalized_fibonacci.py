"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-02
                Capitalized Fibonacci
Given a string, return a new string where each letter is capitalized if its index is a Fibonacci number, and lowercased otherwise.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

The first character is at index 0.
If the index of non-letter characters is a Fibonacci number, leave it unchanged.
"""
def capitalize_fibonacci(s):
    res = []
    fibs = set()
    a = 0
    b = 1
    while a < len(s):
        fibs.add(a)
        temp = b
        b = a + b
        a = temp

    for i, ch in enumerate(s):
        if i in fibs:
            res.append(ch.upper())
        else:
            res.append(ch.lower())
    return "".join(res)

print(capitalize_fibonacci("hello world")) # should return "HELLo woRld".
print(capitalize_fibonacci("HELLO WORLD")) # should return "HELLo woRld".
print(capitalize_fibonacci("hello, world!")) # should return "HELLo, wOrld!".
print(capitalize_fibonacci("The quick brown fox jumped over the lazy dog.")) # should return "THE qUicK broWn fox jUmped over thE lazy dog.".
print(capitalize_fibonacci("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar ex nibh, vel ullamcorper ligula egestas quis. Integer tincidunt fringilla accumsan. Integer et metus placerat, gravida felis at, pellentesque nisl.")) # should return "LOREm ipSum dOlor sit amet, consecTetur adipiscing elit. proin pulvinar ex nibh, vel ullaMcorper ligula egestas quis. integer tincidunt fringillA accumsan. integer et metus placerat, gravida felis at, pellentesque nisl.".