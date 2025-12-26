"""
Docstring for december.snowflake_generator
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-25
                            Snowflake Generator
Given a multi-line string that uses newline characters (\n) to represent a line break, return a new string where each line is mirrored horizontally and attached to the end of the original line.

Mirror a line by reversing all of its characters, including spaces.
For example, given "* \n *\n* ", which logs to the console as:

* 
 *
* 
Return "*  *\n ** \n*  *", which logs to the console as:

*  *
 ** 
*  *
Take careful note of the whitespaces in the given and returned strings. Be sure not to trim any of them.
"""
def generate_snowflake(crystals):
    lines = crystals.split("\n")
    return "\n".join([line + line[::-1] for line in lines])
print(generate_snowflake("* \n *\n* ")                       )     # should return "*  *\n ** \n*  *".
print(generate_snowflake("X=~")                              )     # should return "X=~~=X".
print(generate_snowflake(" X  \n  v \nX--=\n  ^ \n X  ")     )     # should return " X    X \n  v  v  \nX--==--X\n  ^  ^  \n X    X ".
print(generate_snowflake("*   *\n * * \n* * *\n * * \n*   *"))     # should return "*   **   *\n * *  * * \n* * ** * *\n * *  * * \n*   **   *".
print(generate_snowflake("*  -\n * -\n*  -")                 )     # should return "*  --  *\n * -- * \n*  --  *".