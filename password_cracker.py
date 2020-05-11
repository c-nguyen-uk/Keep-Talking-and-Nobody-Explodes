# -*- coding: utf-8 -*-
"""
This programme solves the Password Cracker module.

We do not discriminate between letter capitalisation or input - as long
as there is a comma between them. 

There is also some input forgiveness - if no password can be found,
then retrying is possible.
"""

# We create a list of all possible passwords.

passwords = ["ABOUT", "AFTER", "AGAIN", "BELOW", "COULD", "EVERY", "FIRST",
             "FOUND", "GREAT", "HOUSE", "LARGE", "LEARN", "NEVER", "OTHER",
             "PLACE", "PLANT", "POINT", "RIGHT", "SMALL", "SOUND", "SPELL",
             "STILL", "STUDY", "THEIR", "THERE", "THESE", "THING", "THINK",
             "THREE", "WATER", "WHERE", "WHICH", "WORLD", "WOULD", "WRITE"]

# This simple function checks for a password from any possible
# combinations of letters. Despite being O(n^5), it runs quickly since
# n = 6 in this module. Note that in this module answers are unique.

def password_cracker(L1, L2, L3, L4, L5):
    for i1 in L1:
        for i2 in L2:
            for i3 in L3:
                for i4 in L4:
                    for i5 in L5:
                        if i1 + i2 + i3 + i4 + i5 in passwords:
                            return (i1 + i2 + i3 + i4 + i5)

# We now ask for the sets of letters.

while True:
    L1 = list(input("First letters, separated by a comma: ").upper())
    L2 = list(input("Second letters, separated by a comma: ").upper())
    L3 = list(input("Third letters, separated by a comma: ").upper())
    L4 = list(input("Fourth letters, separated by a comma: ").upper())
    L5 = list(input("Fifth letters, separated by a comma: ").upper())
    while not (password_cracker(L1, L2, L3, L4, L5) in passwords):
        input("No password exists. Press enter to try again.")
        L1 = list(input("First letters, separated by a comma: ").upper())
        L2 = list(input("Second letters, separated by a comma: ").upper())
        L3 = list(input("Third letters, separated by a comma: ").upper())
        L4 = list(input("Fourth letters, separated by a comma: ").upper())
        L5 = list(input("Fifth letters, separated by a comma: ").upper())
    input("The password is: " + password_cracker(L1, L2, L3, L4, L5)
          + "\n \nPress Enter to retry.")
