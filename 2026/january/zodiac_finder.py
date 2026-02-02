"""
Docstring for 2026.january.zodiac_finder
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-31
Zodiac Finder
Given a date string in the format "YYYY-MM-DD", return the zodiac sign for that date using the following chart:

Date Range	Zodiac Sign
March 21 - April 19	"Aries"
April 20 - May 20	"Taurus"
May 21 - June 20	"Gemini"
June 21 - July 22	"Cancer"
July 23 - August 22	"Leo"
August 23 - September 22	"Virgo"
September 23 - October 22	"Libra"
October 23 - November 21	"Scorpio"
November 22 - December 21	"Sagittarius"
December 22 - January 19	"Capricorn"
January 20 - February 18	"Aquarius"
February 19 - March 20	"Pisces"
Zodiac signs are based only on the month and day, you can ignore the year.
"""
def get_sign(date_str):
    year, month, day = date_str.split("-")
    month = int(month)
    day = int(day)

    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    else:
        return "Pisces"

print(get_sign("2026-01-31")) # should return "Aquarius".
print(get_sign("2001-06-10")) # should return "Gemini".
print(get_sign("1985-09-07")) # should return "Virgo".
print(get_sign("2023-03-19")) # should return "Pisces".
print(get_sign("2045-11-05")) # should return "Scorpio".
print(get_sign("1985-12-06")) # should return "Sagittarius".
print(get_sign("2025-12-30")) # should return "Capricorn".
print(get_sign("2018-10-08")) # should return "Libra".
print(get_sign("1958-05-04")) # should return "Taurus".