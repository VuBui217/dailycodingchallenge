"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-24
                    Passing Exam Count
Given an array of student exam scores and the score needed to pass it, return the number of students that passed the exam.
"""
def passing_count(scores, passing_score):

    return sum(score >= passing_score for score in scores)

print(passing_count([90, 85, 75, 60, 50], 70)) # should return 3.
print(passing_count([100, 80, 75, 88, 72, 74, 79, 71, 60, 92], 75)) # should return 6.
print(passing_count([79, 60, 88, 72, 74, 59, 75, 71, 80, 92], 60)) # should return 9.
print(passing_count([76, 79, 80, 70, 71, 65, 79, 78, 59, 72], 85)) # should return 0.
print(passing_count([84, 65, 98, 53, 58, 71, 91, 80, 92, 70, 73, 83, 86, 69, 84, 77, 72, 58, 69, 75, 66, 68, 72, 96, 90, 63, 88, 63, 80, 67], 60)) # should return 27.