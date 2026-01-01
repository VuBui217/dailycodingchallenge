"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-27

What's My Age Again?
Given the date of someone's birthday in the format YYYY-MM-DD, return the person's age as of November 27th, 2025.

Assume all birthdays are valid dates before November 27th, 2025.
Return the age as an integer.
Be sure to account for whether the person has already had their birthday in 2025.
"""
def calculate_age(birthday):
    year, month, date = birthday.split("-")

    curr_year, curr_month, curr_date = 2025, 11, 27
    

    if (curr_month > int(month)) or (curr_month == int(month) and curr_date >= int(date)):
        age = curr_year - int(year)
    else:
        age = curr_year - int(year) - 1

    return age

calculate_age("2000-11-20")    #should return 25.
calculate_age("2000-12-01")    #should return 24.
calculate_age("2014-10-25")    #should return 11.
calculate_age("1994-01-06")    #should return 31.
calculate_age("1994-12-14")    #should return 30.