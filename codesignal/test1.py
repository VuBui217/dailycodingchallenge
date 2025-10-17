"""
Problem 1
"""
def problem1_solution1(text: str) -> int:
    """Count words whose first and last characters match (case-insensitive)."""
    count = 0
    start = 0
    text += " "  # sentinel space so the final word is evaluated

    for idx, char in enumerate(text):
        if char == " ":
            # Skip consecutive spaces (empty words)
            if idx > start:
                first = text[start]
                last = text[idx - 1]
                if first.lower() == last.lower():
                    count += 1
            start = idx + 1

    return count

def problem1_solution2(strs):
    count = 0
    lst = strs.split(' ')

    for s in lst:
        if s[0].lower() == s[-1].lower():
            count+=1
    return count
sample = "L0dfdfdfl world BoB" 
print(problem1_solution1(sample))
print(problem1_solution2(sample))



