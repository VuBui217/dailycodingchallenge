"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-15

                                HTML Tag Stripper
Given a string of HTML code, remove the tags and return the plain text content.

The input string will contain only valid HTML.
HTML tags may be nested.
Remove the tags and any attributes.
For example, '<a href="#">Click here</a>' should return "Click here".

"""
def strip_tags(html):
    # here is the key to solve this problem
    # use this to flag if the curr is in tag
    in_tag = False 
    output = []

    i = 0

    n = len(html)

    while i<n:
        if not in_tag and html[i]=='<':
            in_tag = True
        elif in_tag and html[i]=='>':
            in_tag =False
        elif not in_tag:
            output+=html[i]

        i+=1
    return ''.join(output)

#Test
"""
strip_tags('<a href="#">Click here</a>') should return "Click here".
trip_tags('<p class="center">Hello <b>World</b>!</p>') should return "Hello World!".
strip_tags('<img src="cat.jpg" alt="Cat">') should return an empty string ("").
strip_tags('<main id="main"><section class="section">section</section><section class="section">section</section></main>') should return sectionsection.
"""