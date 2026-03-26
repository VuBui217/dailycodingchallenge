"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-26
                    Movie Night
Given a string for the day of the week, another string for a showtime, and an integer number of tickets, return the total cost of the movie tickets for that showing.

The given day will be one of:

"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
"Sunday"
The showtime will be given in the format "H:MMam" or "H:MMpm". For example "10:00am" or "10:00pm".

Return the total cost in the format "$D.CC" using these rules:

Weekend (Friday - Sunday): $12.00 per ticket.
Weekday (Monday - Thursday): $10.00 per ticket.
Matinee (before 5:00pm): subtract $2.00 per ticket (except on Tuesdays).
Tuesdays: all tickets are $5.00 each.
"""
def get_movie_night_cost(day, showtime, number_of_tickets):
    total = 0

    if day == "Tuesday":
        total = number_of_tickets * 5

    else:
        hh, mm = map(int, showtime[:-2].split(':'))
        am_or_pm = showtime[-2:]

        is_matinee = (am_or_pm == "am") or (am_or_pm == "pm" and (hh == 12 or hh < 5))
        base = 12 if day in ["Friday", "Saturday", "Sunday"] else 10
        price = base - 2 if is_matinee else base
        total = price * number_of_tickets 
    
    return f"${total:.2f}"

print(get_movie_night_cost("Saturday", "10:00pm", 1)) # should return "$12.00".
print(get_movie_night_cost("Sunday", "10:00am", 1))   # should return "$10.00".
print(get_movie_night_cost("Tuesday", "7:20pm", 2))    # should return "$10.00".
print(get_movie_night_cost("Wednesday", "5:40pm", 3))  # should return "$30.00".
print(get_movie_night_cost("Monday", "11:50am", 4)) # should return "$32.00".
print(get_movie_night_cost("Friday", "4:30pm", 5))   # should return "$50.00".
print(get_movie_night_cost("Tuesday", "11:30am", 1))   # should return "$5.00"
