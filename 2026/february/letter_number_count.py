"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-26
                    Letter and Number Count
Given a string, return a message with the count of how many letters and numbers it contains.

Letters are A-Z and a-z.
Numbers are 0-9.
Ignore all other characters.
Return "The string has X letters and Y numbers.", where "X" is the count of letters and "Y" is the count of numbers. If either count is 1, use the singular form for that item. E.g: "1 letter" instead of "1 letters" and "1 number" instead of "1 numbers".
"""
def count_letters_and_numbers(s):
    letter_count = 0
    number_count = 0

    for ch in s:
        if ch.isdigit():
            number_count += 1
        elif ch.isalpha():
            letter_count += 1
    num_str = 'number' if number_count == 1 else 'numbers'
    letter_str = 'letter' if letter_count == 1 else 'letters'

    return f"The string has {letter_count} {letter_str} and {number_count} {num_str}."
