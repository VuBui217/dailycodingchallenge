"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-20
                        Equinox Shadows
Today is the equinox, when the sun is directly above the equator and perfectly overhead at noon. Given a time, determine the shadow cast by a 4-foot vertical pole.

The time will be a string in "HH:MM" 24-hour format (for example, "15:00" is 3pm).
You will only be given a time in 30 minute increments.
Rules:

The sun rises at 6am directly "east", and sets at 6pm directly "west".
A shadow always points opposite the sun.
The shadow's length (in feet) is the number of hours away from noon, cubed.
There is no shadow before sunrise (before 6am), after sunset (6pm or later), or at noon.
Return:

If a shadow exists, return "(length)ft (direction)". For example, "8ft west".
Otherwise, return "No shadow".
For example, given "10:00", return "8ft west" because 10am is 2 hours from noon, so 23 = 8 feet, and the shadow points west because the sun is in the east at 10am.
"""
def get_shadow(time):
    hh, mm = map(int, time.split(':'))

    if hh < 6 or (hh == 12 and mm == 0) or hh >= 18:
        return 'No shadow'
    
    if hh < 12:
        direction = 'west'
        if mm == 0:
            length = (12 - hh) ** 3
        else:
            length = round((11 - hh + 0.5) ** 3, 3)
    else:
        direction = 'east'
        if mm == 0:
            length = (hh - 12) ** 3
        else:
            length = round((hh - 12 + 0.5) ** 3, 3)
    return f"{length}ft {direction}"