"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-31

                                                    SpOoKy~CaSe
Given a string representing a variable name, convert it to "spooky case" using the following constraints:

Replace all underscores (_), and hyphens (-) with a tilde (~).
Capitalize the first letter of the string, and every other letter after that, ignore the tilde character when counting.
For example, given hello_world, return HeLlO~wOrLd.

"""

def spookify(boo):
    lst = list(boo.lower())
    ch_count = 0
    for i in range(len(lst)):
        if lst[i].isalpha():
            ch_count +=1
            if ch_count % 2 == 1:
                lst[i] = lst[i].upper()
        elif lst[i] == '_' or lst[i] == '-':
            lst[i] = '~'

        
    return ''.join(lst)


print(spookify("TRICK-or-TREAT"))

print(spookify("hello_world"))