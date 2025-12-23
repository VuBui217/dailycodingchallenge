"""
Docstring for december.email_chain_count
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-23
                            Re: Fwd: Fw: Count
Given a string representing the subject line of an email, determine how many times the email has been forwarded or replied to.

For simplicity, consider an email forwarded or replied to if the string contains any of the following markers (case-insensitive):

"fw:"
"fwd:"
"re:"
Return the total number of occurrences of these markers.
"""
def email_chain_count(subject):
    subject = subject.lower()
    count = 0
    for marker in ["fw:", "fwd:", "re:"]:
        count += subject.count(marker)
    return count

print(email_chain_count("Re: Meeting Notes")) # should return 1.
print(email_chain_count("Meeting Notes")) # should return 0.
print(email_chain_count("Re: re: RE: rE: Meeting Notes")) # should return 4.
print(email_chain_count("Re: Fwd: Re: Fw: Re: Meeting Notes")) # should return 5.
print(email_chain_count("re:Ref:fw:re:review:FW:Re:fw:report:Re:FW:followup:re:summary:Fwd:Re:fw:NextStep:RE:FW:re:Project:Fwd:Re:fw:Notes:RE:re:Update:FWD:Re:fw:Summary")) # should return 23.