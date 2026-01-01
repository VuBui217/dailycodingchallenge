"""
Docstring for december.date_formatter
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-06

Date Formatter
Given a date in the format "Month day, year", return the date in the format "YYYY-MM-DD".

The given month will be the full English month name. For example: "January", "February", etc.
In the return value, pad the month and day with leading zeros if necessary to ensure two digits.
For example, given "December 6, 2025", return "2025-12-06".
"""
def format_date(date_string):
    string_list = date_string.split()
    month = string_list[0]
    day = string_list[1].rstrip(",")
    year = string_list[2]

    month_map = {"January" : "01", "February": "02", "March": "03", "April": "04", "May": "05", "June": "06", "July": "07", "August": "08", "September": "09", "October": "10", "November": "11", "December": "12"}

    if int(day) < 10:
        day = "0" + day

    return f"{year}-{month_map[month]}-{day}"

print(format_date("December 6, 2025") )        # should return "2025-12-06".
print(format_date("January 1, 2000")  )        # should return "2000-01-01".
print(format_date("November 11, 1111"))        # should return "1111-11-11".
print(format_date("September 7, 512") )        # should return "512-09-07".
print(format_date("May 4, 1950")      )        # should return "1950-05-04".