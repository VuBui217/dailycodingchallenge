"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-20

                                Longest Word
Given a sentence string, return the longest word in the sentence.

Words are separated by a single space.
Only letters (a-z, case-insensitive) count toward the word's length.
If there are multiple words with the same length, return the first one that appears.
Return the word as it appears in the given string, with punctuation removed.
"""
# Bute force O(n*m)
def longest_word(sentence):
    max_len = 0
    output = ""
    word_list = sentence.split()

    for word in word_list:
        ch_count = 0
        curr = ""
        for ch in word:
            if ch.isalpha():
                ch_count += 1
                curr += ch
        if ch_count > max_len:
            max_len = ch_count
            output = curr
    return output

# Optimized solution 1 pass, O(n) (n is number of charaters in given sentence), no extra space
def optimized_longest_word(sentence):
    max_len = 0
    output = ""
    curr_len = 0
    curr_word = ""

    i = 0

    for ch in sentence + " ":
        if ch.isalpha():
            curr_len += 1
            curr_word += ch
        elif ch == " ":
            if curr_len > max_len:
                max_len = curr_len
                output = curr_word
            curr_len = 0
            curr_word = ""
        else:
            continue
    return output

longest_word("The quick red fox")           # should return "quick".
longest_word("Hello coding challenge.")     # should return "challenge".
longest_word("Do Try This At Home.")        # should return "This".
longest_word("This sentence... has commas, ellipses, and an exlamation point!") # should return "exlamation".
longest_word("A tie? No way!")              # should return "tie".
longest_word("Wouldn't you like to know.")  # should return "Wouldnt"
        