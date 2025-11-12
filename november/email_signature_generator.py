"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-12
                                            Email Signature Generator
Given strings for a person's name, title, and company, return an email signature as a single string using the following rules:

The name should appear first, preceded by a prefix that depends on the first letter of the name. For names starting with (case-insensitive):
A-I: Use >> as the prefix.
J-R: Use -- as the prefix.
S-Z: Use :: as the prefix.
A comma and space (, ) should follow the name.
The title and company should follow the comma and space, separated by " at " (with spaces around it).
For example, given "Quinn Waverly", "Founder and CEO", and "TechCo" return "--Quinn Waverly, Founder and CEO at TechCo".
"""
def generate_signature(name, title, company):
    name_with_prefix = ""

    name_first_letter = name[0].upper()

    if ord('A') <= ord(name_first_letter) <= ord('I'):
        name_with_prefix = ">>" + name
    elif ord('J') <= ord(name_first_letter) <= ord('R'):
        name_with_prefix = "--" + name
    elif ord('S') <= ord(name_first_letter) <= ord('Z'):
        name_with_prefix = "::" + name
    else:
        name_with_prefix = name

    result = f"{name_with_prefix}, {title} at {company}"
    return result

# print(generate_signature("Quinn Waverly", "Founder and CEO", "TechCo")    )    #should return "--Quinn Waverly, Founder and CEO at TechCo".
# print(generate_signature("Alice Reed", "Engineer", "TechCo")              )    #should return ">>Alice Reed, Engineer at TechCo".
# print(generate_signature("Tina Vaughn", "Developer", "example.com")       )    #should return "::Tina Vaughn, Developer at example.com".
# print(generate_signature("B. B.", "Product Tester", "AcmeCorp")           )    #should return ">>B. B., Product Tester at AcmeCorp".
# print(generate_signature("windstorm", "Cloud Architect", "Atmospheronics"))    #should return "::windstorm, Cloud Architect at Atmospheronics"