"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-28
                                                    Navigator
On October 28, 1994, Netscape Navigator was released, helping millions explore the early web.

Given an array of browser commands you executed on Netscape Navigator, return the current page you are on after executing all the commands using the following rules:

You always start on the "Home" page, which will not be included in the commands array.
Valid commands are:
"Visit Page": Where "Page" is the name of the page you are visiting. For example, "Visit About" takes you to the "About" page. When you visit a new page, make sure to discard any forward history you have.
"Back": Takes you to the previous page in your history or stays on the current page if there isn't one.
"Forward": Takes you forward in the history to the page you came from or stays on the current page if there isn't one.
For example, given ["Visit About Us", "Back", "Forward"], return "About Us".
"""
def navigate(commands):
    curr_page = 'Home'
    back = [] # a stack stores pages we can go back to
    forward = [] # a stack stores page we can go forward to

    for cmd in commands:
        # visit command
        if cmd.startswith('Visit '):
            page = cmd[6:]
            back.append(curr_page)
            forward.clear()
            curr_page = page
        elif cmd == 'Back':
            if back:
                forward.append(curr_page)
                curr_page = back.pop()
        elif cmd == 'Forward':
            if forward:
                back.append(curr_page)
                curr_page = forward.pop()
    
    return curr_page


#test cases
print(navigate(["Visit About Us", "Back", "Forward"])                                      )   #should return "About Us".
print(navigate(["Forward"])                                                                )   #should return "Home".
print(navigate(["Back"])                                                                   )   #should return "Home".
print(navigate(["Visit About Us", "Visit Gallery"])                                        )   #should return "Gallery".
print(navigate(["Visit About Us", "Visit Gallery", "Back", "Back"])                        )   #should return "Home".
print(navigate(["Visit About", "Visit Gallery", "Back", "Visit Contact", "Forward"])       )   #should return "Contact".
print(navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"]))   #hould return "Visit Us".






