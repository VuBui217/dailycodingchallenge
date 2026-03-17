"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-17
                    Anniversary Milestones
Given an integer representing the number of years a couple has been married, return their most recent anniversary milestone according to this chart:

Years Married	Milestone
1	            "Paper"
5	            "Wood"
10	            "Tin"
25	            "Silver"
40	            "Ruby"
50	            "Gold"
60	            "Diamond"
70	            "Platinum"
If they haven't reached the first milestone, return "Newlyweds".
"""
def get_milestone(years):
    years_milestone = [(0, "Newlyweds"), (1, "Paper"), (5, "Wood"), (10, "Tin"),
              (25, "Silver"), (40, "Ruby"), (50, "Gold"), (60, "Diamond"), (70, "Platinum")]

    if years < 0:
        return 'Invalid year'
    recent_milestone = None
    for year, milestone in years_milestone:
        if years >= year:
            recent_milestone = milestone
        else:
            break
    return recent_milestone

print(get_milestone(0))    # should return "Newlyweds".
print(get_milestone(1))    # should return "Paper".
print(get_milestone(8))    # should return "Wood".
print(get_milestone(10))   # should return "Tin".
print(get_milestone(26))   # should return "Silver".
print(get_milestone(45))   # should return "Ruby".
print(get_milestone(50))   # should return "Gold".
print(get_milestone(64))   # should return "Diamond".
print(get_milestone(71))   # should return "Platinum".