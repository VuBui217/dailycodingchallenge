"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-23
                    Blood Type Compatibility
Given a donor blood type and a recipient blood type, determine whether the donor can give blood to the recipient.

Each blood type consists of:

A letter: "A", "B", "AB", or "O"
And an Rh factor: "+" or "-"
Blood types will be one of the valid letters followed by an Rh factor. For example, "AB+" and "O-" are valid blood types.

Letter Rules:

"O" can donate to other letter type.
"A" can donate to "A" and "AB".
"B" can donate to "B" and "AB".
"AB" can donate only to "AB".
Rh Rules:

Negative ("-") can donate to both "-" and "+".
Positive ("+") can donate only to "+".
Both letter and Rh rule must pass for a donor to be able to donate to the recipient.
"""
def can_donate(donor, recipient):
    donor_letter = donor[:-1]
    donor_rh = donor[-1]

    recipient_letter = recipient[:-1]
    recipient_rh = recipient[-1]

    # Letter rules
    if donor_letter == 'A' and recipient_letter not in ['A', 'AB']:
        return False
    if donor_letter == 'B' and recipient_letter not in ['B', 'AB']:
        return False
    if donor_letter == 'AB' and recipient_letter != 'AB':
        return False

    # Rh rules
    if donor_rh == '+' and recipient_rh != '+':
        return False

    return True

print(can_donate("B+", "B+")  )    # should return True.
print(can_donate("O-", "AB-") )    # should return True.
print(can_donate("O+", "A-")  )    # should return False.
print(can_donate("A+", "AB+") )    # should return True.
print(can_donate("A-", "B-")  )    # should return False.
print(can_donate("B-", "AB+") )    # should return True.
print(can_donate("B-", "A+")  )    # should return False.
print(can_donate("O-", "O+")  )    # should return True.
print(can_donate("O+", "O-")  )    # should return False.
print(can_donate("AB+", "AB-"))    # should return False.