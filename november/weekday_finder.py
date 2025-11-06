"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-06

                                            Weekday Finder
Given a string date in the format YYYY-MM-DD, return the day of the week.

Valid return days are:

"Sunday"
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
Be sure to ignore time zones.
"""
def get_weekday(date_string):
    import datetime

    # extract year, month, date
    year, month, date = map(int, date_string.split('-'))

    # Parse input into a date object
    date_obj = datetime.date(year, month, date)

    # Get the weekday index (Monday = 0, Sunday = 6)
    weekday_idx = date_obj.weekday()

    # Map the index to the required weekday names
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    return days[weekday_idx]

# get_weekday("2025-11-06")           #should return Thursday.
# get_weekday("1999-12-31")           #should return Friday.
# get_weekday("1111-11-11")           #should return Saturday.
# get_weekday("2112-12-21")           #should return Wednesday.
# get_weekday("2345-10-01")           #should return Monday.
