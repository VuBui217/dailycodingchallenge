"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-16
                    String Math
Given a string with numbers and other characters, perform math on the numbers based on the count of non-digit characters between the numbers.

If the count of characters separating two numbers is even, use addition.
If it's odd, use subtraction.
Consecutive digits form a single number.
Operations are applied left to right.
Ignore leading and trailing characters that aren't digits.
For example, given "3ab10c8", return 5. Add 3 and 10 to get 13 because there's an even number of characters between them. Then subtract 8 from 13 because there's an odd number of characters between the result and 8.
"""
def do_math(s):
    # validate input
    if not any(c.isdigit() for c in s):
        return 0
    # Normalize input s
    left = 0
    right = len(s) - 1
    while left < right and not s[left].isdigit():
        left += 1
    while left < right and not s[right].isdigit():
        right -= 1
    
    s = s[left: right+1]

    # Scan the array
    output = 0
    is_pos = True
    i = j = 0
    while j < len(s):
        while j < len(s) and s[j].isdigit():
            j += 1
        num = int(s[i:j]) 
        # print(num)
        if is_pos:
            output += num
        else:
            output -= num
        # print(output)
        i = j 
        while j < len(s) and not s[j].isdigit():
            j += 1
        if (j-i) % 2 == 1:
            is_pos = False
        else:
            is_pos = True
        i = j
        
    return output
print(do_math("3ab10c8")) # should return 5.
print(do_math("6MINUS4")) # should return 2.
print(do_math("9plus3")) # should return 12.
print(do_math("5fkwo#10i#%.<>15P=@20!#B/25")) # should return 15.
print(do_math("a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt")) # should return 67.