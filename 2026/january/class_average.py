"""
Docstring for 2026.january.class_average
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-22
                        Class Average
Given an array of exam scores (numbers), return the average score in form of a letter grade according to the following chart:

Average Score	Letter Grade
97-100	            "A+"
93-96	            "A"
90-92	            "A−"
87-89	            "B+"
83-86	            "B"
80-82	            "B-"
77-79	            "C+"
73–76	            "C"
70-72	            "C-"
67-69	            "D+"
63-66	            "D"
60–62	            "D-"
below 60	        "F"
Calculate the average by adding all scores in the array and dividing by the total number of scores.
"""
def get_average_grade(scores):
    average = round(sum(scores) / len(scores))
  
    if 97 <= average <= 100:
        return "A+"
    elif 93 <= average <= 96:
        return "A"
    elif 90 <= average <= 92:
        return "A-"
    elif 87 <= average <= 89:
        return "B+"
    elif 83 <= average <= 86:
        return "B"
    elif 80 <= average <= 82:
        return "B-"
    elif 77 <= average <= 79:
        return "C+"
    elif 73 <= average <= 76:
        return "C"
    elif 70 <= average <= 72:
        return "C-"
    elif 67 <= average <= 69:
        return "D+"
    elif 63 <= average <= 66:
        return "D"
    elif 60 <= average <= 62:
        return "D-"
    else:
        return "F"
    
print(get_average_grade([92, 91, 90, 94, 89, 93])              )   # should return "A-".
print(get_average_grade([84, 89, 85, 100, 91, 88, 79])         )   # should return "B+".
print(get_average_grade([63, 69, 65, 66, 71, 64, 65])          )   # should return "D".
print(get_average_grade([97, 98, 99, 100, 96, 97, 98, 99, 100]))   # should return "A+".
print(get_average_grade([75, 100, 88, 79, 80, 78, 64, 60])     )   # should return "C+".
print(get_average_grade([45, 48, 50, 52, 100, 54, 56, 58, 59]) )   # should return "F".