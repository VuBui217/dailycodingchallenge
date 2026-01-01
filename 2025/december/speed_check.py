"""
Docstring for december.speed_check
                    Speed Check
Given the speed you are traveling in miles per hour (MPH), and a speed limit in kilometers per hour (KPH), determine whether you are speeding and if you will get a warning or a ticket.

1 mile equals 1.60934 kilometers.
If you are travelling less than or equal to the speed limit, return "Not Speeding".
If you are travelling 5 KPH or less over the speed limit, return "Warning".
If you are travelling more than 5 KPH over the speed limit, return "Ticket".
"""
def speed_check(speed_mph, speed_limit_kph):
    speed = speed_mph * 1.60934
    diff = speed - speed_limit_kph
    if diff <= 0:
        return "Not Speeding"
    elif 0 < diff <= 5:
        return "Warning"
    else:
        return "Ticket"
print(speed_check(30, 70) )    # should return "Not Speeding".
print(speed_check(40, 60) )   # should return "Warning".
print(speed_check(40, 65) )   # should return "Not Speeding".
print(speed_check(60, 90) )   # should return "Ticket".
print(speed_check(65, 100))   # should return "Warning".
print(speed_check(88, 40) )   # should return "Ticket".