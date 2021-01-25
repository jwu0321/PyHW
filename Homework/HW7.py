# YOUR NAME HERE

"""
Problem 1
Pretend you have a flip phone that uses multiple button presses to get a character.
Here's a table mapping the button to the characters:
Key   Character
1     .,?!:
2     ABC
3     DEF
4     GHI
5     JKL
6     MNO
7     PQRS
8     TUV
9     WXYZ
0     Space
For instance, pressing 4 twice gets 'H'.
Implement the function to use a dictionary to turn a string into a string of button presses. 'Hello, World!' becomes
4433555555666110966677755531111. Account for both uppercase and lowercase letters. The button's don't differentiate
for capitalization, you can adjust the input for the table. You can ignore every other that's not shown in the table.
"""


def flip_phone(message):
    return None


"""
Problem 2
Use one or more dictionaries to see how many unique characters are in a string.
For instance, 'zzz' has one unique character while 'Hello, World!' has 10. 
"""


def unique_characters(string):
    return None


"""
Problem 3
Create a Car class with the attributes brand, max_speed, and current_speed. Initialize all those attributes in its
constructor in that order. Add two methods, accelerate and decelerate, which take no parameters, 
and add 10 to current_speed in accelerate and subtract 5 in decelerate. Check if accelerating will go past max_speed 
and if decelerating will make it go past 0. If either situation happens, don't change the speed.
"""