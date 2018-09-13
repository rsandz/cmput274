# ===================================================
# Assignment 1: Password Validator and Generator 
# ===================================================
# Name: Ryan Sandoval
# Course: CMPUT 274
# Section: LBL EA1

import re

MIN_LENGTH = 8

def validate(password):
    """ Analyzes an input password to determine if it is "Secure", 
    "Insecure", or "Invalid" based on the assignment description 
    criteria.

    Arguments:
        password (string): a string of characters

    Returns:
        result (string): either "Secure", "Insecure", or "Invalid". 
    """
    
    # Check if invalid length
    if (len(password) < MIN_LENGTH):
        return("Invalid")

    # Check pattern
    invalidPattern = re.compile("[ _-]")
    if invalidPattern.search(password) != None:
        return("Invalid")

def generate(n):
    """ Generates a password of length n which is guaranteed to 
    be Secure according to the given criteria.

    Arguments:
        n (integer): the length of the password to generate, n >= 8.

    Returns:
        secure_password (string): a Secure password of length n. 
    """
    pass

if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 validator.py". This can be useful for
    # testing your implementations by calling them here.

    print(validate(input()))