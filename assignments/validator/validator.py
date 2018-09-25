# ===================================================
# Exercise 1: Password Validator and Generator
# ===================================================
# Name: Ryan Sandoval
# ID: 1529017
# Course: CMPUT 274, FALL 2018

import re
import random
import string

# (integer) Minimum VALID Password length
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

    # Check if Invalid
    # ================

    if (len(password) < MIN_LENGTH):
        return("Invalid")

    # Check for invalid regex pattern
    invalidPattern = re.compile("[ _-]")
    if invalidPattern.search(password) is not None:
        return("Invalid")

    # Check if Secure
    # =================

    patterns = [
        re.compile(r"[A-Z]"),  # Uppercase Character Pattern
        re.compile(r"[a-z]"),  # Lowercase Character Pattern
        re.compile(r"[0-9]"),  # Decimal Pattern
        re.compile(r"[!#$%&'()*+,./:;<=>?@[\]^`{|}~]")  # Symbol Pattern
    ]

    # Check if the password has a match with all the above pattenrs
    # If one pattern fails to match, the password is insecure

    for pattern in patterns:
        if pattern.search(password) is None:
            return("Insecure")

    # If program got here, password passed
    return("Secure")


def generate(n):
    """ Generates a password of length n which is guaranteed to
    be Secure according to the given criteria.

    Arguments:
        n (integer): the length of the password to generate, n >= 8.

    Returns:
        secure_password (string): a Secure password of length n.
    """

    # Note: Each character type will make up roughly 1/4 of the password

    # Init
    type = 0
    password = []
    symbols = r"!#$%&'()*+,./:;<=>?@[\]^`{|}~"

    # Error if Invalid n
    if n < MIN_LENGTH:
        raise ValueError(
            "Argument 'n' must be " + str(MIN_LENGTH) + " or greater"
        )

    # Generate the password
    while (len(password) != n):

        # Generate Random Uppercase Char
        if type == 0:
            password.append(string.ascii_uppercase[random.randint(0, 25)])

        # Generate Random Lowercase Char
        elif type == 1:
            password.append(string.ascii_lowercase[random.randint(0, 25)])

        # Generate Random Decimal
        elif type == 2:
            password.append(str(random.randint(0, 9)))

        # Generate Random Symbol
        elif type == 3:
            index = random.randint(0, len(symbols) - 1)
            password.append(symbols[index])

        # Step the type (So we can have different types in the password)
        type = (type + 1) % 4

    # Shuffle the Password to remove the type pattern
    random.shuffle(password)

    return("".join(password))


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 validator.py". This can be useful for
    # testing your implementations by calling them here.
    pass
