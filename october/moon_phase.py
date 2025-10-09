"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-09

                                    Space Week Day 6: Moon Phase
For day six of Space Week, you will be given a date in the format "YYYY-MM-DD" and need to determine the phase of the moon for that day using the following rules:

Use a simplified lunar cycle of 28 days, divided into four equal phases:

"New": days 1 - 7
"Waxing": days 8 - 14
"Full": days 15 - 21
"Waning": days 22 - 28
After day 28, the cycle repeats with day 1, a new moon.

Use "2000-01-06" as a reference new moon (day 1 of the cycle) to determine the phase of the given day.
You will not be given any dates before the reference date.
Return the correct phase as a string.
"""

def moon_phase(date_string):
    curr_y, curr_m, curr_d = map(int, date_string.split('-'))

    ref_y, ref_m, ref_d = 2000, 1, 6

    #days in 12 months for regular year
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    
    def days_since_ref(year,month,date):
        days = 0
        
        #year
        for y in range(2000, year+1):
            if y%4 == 0 and (y%100!=0 or y%400 ==0):
                days+=366
            else:
                days+=365
    
        #month
        for m in range(month-1):
            if m==1 and (year%4 == 0 and (year%100!=0 or year%400 ==0)):
                days+=29
            else:
                days+=months[m]
        #day
        days+=date
        return days

    total_days = days_since_ref(curr_y, curr_m, curr_d) - days_since_ref(ref_y, ref_m, ref_d)

    cycle_day = (total_days%28) + 1 # we start at day 1 to 28 so plus 1

    if cycle_day in range(1,8):
        return 'New'
    elif cycle_day in range(8,15):
        return 'Waxing'
    elif cycle_day in range(15,22):
        return 'Full'
    else:
        return 'Waning'
    
print(moon_phase("2014-10-15"))