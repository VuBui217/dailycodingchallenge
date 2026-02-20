"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-20
                    2026 Winter Games Day 15: Freestyle Skiing
Given a trick name consisting of two words, determine if it is a valid freestyle skiing trick name.

A trick is valid if the first word is in the list of valid first words, and the second word is in the list of valid second words.

The two words will be separated by a single space.
Valid first words:

"Misty"
"Ghost"
"Thunder"
"Solar"
"Sky"
"Phantom"
"Frozen"
"Polar"
Valid second words:

"Twister"
"Icequake"
"Avalanche"
"Vortex"
"Snowstorm"
"Frostbite"
"Blizzard"
"Shadow"
"""
def is_valid_trick(trick_name):
    first_words = ["Misty", "Ghost", "Thunder", "Solar", "Sky", "Phantom", "Frozen", "Polar"]
    second_words = ["Twister", "Icequake", "Avalanche", "Vortex", "Snowstorm", "Frostbite", "Blizzard", "Shadow"]

    first, second = trick_name.split(" ")

    return first in first_words and second in second_words

print(is_valid_trick("Polar Vortex")     ) # should return True.
print(is_valid_trick("Solar Icequake")   ) # should return True.
print(is_valid_trick("Thunder Blizzard") ) # should return True.
print(is_valid_trick("Phantom Frostbite")) # should return True.
print(is_valid_trick("Ghost Avalanche")  ) # should return True.
print(is_valid_trick("Snowstorm Shadow") ) # should return False.
print(is_valid_trick("Solar Sky")        ) # should return False.