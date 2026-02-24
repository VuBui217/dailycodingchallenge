"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-24
Business Day Count
Given a start date and an end date, return the number of business days between the two.

Given dates are in the format "YYYY-MM-DD".
Weekdays are business days (Monday through Friday).
Weekends are not business days (Saturday and Sunday).
Include both the start and end dates when counting.
"""
def count_business_days(start, end):
    import datetime
    res = 0
    start_year, start_month, start_date = map(int, start.split('-'))
    end_year, end_month, end_date = map(int, end.split('-'))

    start_date_obj = datetime.date(start_year, start_month, start_date)
    end_date_obj = datetime.date(end_year, end_month, end_date)

    curr = start_date_obj
    while curr <= end_date_obj:
        if curr.weekday() < 5:
            res += 1
        curr += datetime.timedelta(days=1)
        
    return res
