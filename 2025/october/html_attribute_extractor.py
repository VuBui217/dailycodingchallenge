"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-19
                                        HTML Attribute Extractor
Given a string of a valid HTML element, return the attributes of the element using the following criteria:

You will only be given one element.
Attributes will be in the format: attribute="value".
Return an array of strings with each attribute property and value, separated by a comma, in this format: ["attribute1, value1", "attribute2, value2"].
Return attributes in the order they are given.
If no attributes are found, return an empty array.

"""
def extract_attributes(element):

    # This solution does not work for the case atribute has spaces in it value
    # output = []

    # #extract the opening tag
    # l=r=1
    # opening_tag = ''
    # while r < len(element):
    #     if element[r] == '/':
    #         opening_tag = element[l:r]
    #         break
    #     elif element[r] == '>':
    #         opening_tag = element[l:r]
    #         break
    #     else:
    #         r+=1
    

    # lst = (opening_tag.strip()).split(' ')
    # print(lst)
    # if len(lst) == 1:
    #     return output
    # for i in range(1,len(lst)):
    #     item = lst[i].replace('"', '')
    #     item = item.replace('=', ', ')
    #     output.append(item)
    # print(output)
    # return output

    # USing regular expression in Python
    import re
    # Extract the opening tag content (between < and >)
    match = re.search(r"<([^>]+)>", element)
    if not match:
        return []
    
    opening_tag = match.group(1).strip()
    print(opening_tag)
    # Find all attribute="value" pairs
    attributes = re.findall(r'(\w+)="([^"]*)"', opening_tag)

    # Format as ["attribute, value", ...]
    return [f"{attr}, {val}" for attr, val in attributes]




extract_attributes('<meta charset="UTF-8" />')

extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>')