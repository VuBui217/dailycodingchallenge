"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-19

Markdown Heading Converter
Given a string representing a Markdown heading, return the equivalent HTML heading.

                                        A valid Markdown heading must:

Start with zero or more spaces, followed by
1 to 6 hash characters (#) in a row, then
At least one space. And finally,
The heading text.
The number of hash symbols determines the heading level. For example, one hash symbol corresponds to an h1 tag, and six hash symbols correspond to an h6 tag.

If the given string doesn't have the exact format above, return "Invalid format".

For example, given "# My level 1 heading", return "<h1>My level 1 heading</h1>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
"""
def convert(heading):
    heading = heading.strip()
    if not heading.startswith('#'):
        return "Invalid format"
    heading_list = heading.split()

    hash_set = set(heading_list[0])
    if not hash_set == {"#"}:
        return "Invalid format"
    if not 1 <= len(heading_list[0]) <= 6:
        return "Invalid format"
    

    num_hash = len(heading_list[0])
    text = ' '.join(heading_list[1:])

    return f"<h{num_hash}>{text}</h{num_hash}>"

# print(convert("# My level 1 heading")     )   #should return "<h1>My level 1 heading</h1>".
# print(convert("My heading")               )   #should return "Invalid format".
# print(convert("##### My level 5 heading") )   #should return "<h5>My level 5 heading</h5>".
# print(convert("#My heading")              )   #should return "Invalid format".
# print(convert("  ###  My level 3 heading"))   #should return "<h3>My level 3 heading</h3>".
# print(convert("####### My level 7 heading"))   #should return "Invalid format".
# print(convert("## My #2 heading")         )   #should return "<h2>My #2 heading</h2>"

