#=====================================
# Hacking
#=====================================
# Version 4
#
# Hacking is a terminal based password
# guessing game
#

# Imports
import uagame
import time

def display_line(window, msg, location, delay = 0.3, updateY = True):
    """
    Prints msg to the uagame Window

    Arguments:
        window (Window): The window to display to
        msg (string): The message to display
        location (tuple): Contains [x, y] values for string
        delay (float): Delay between prints
        updateY (boolean): Whether to update location[1] with new y value

    Return:
        (int) new location
    """
    window.draw_string(msg, location[0], location[1])
    if updateY: location[1] += window.get_font_height()
    window.update()
    time.sleep(0.3)

def getCenteredStringX(window, string):
    """
    Gets X offset needed to center text

    Arguments:
        string (string): String to center

    Return:
        (integer): X Offset for string
    """
    return (window.get_width() - window.get_string_width(string)) // 2

def prompt_user(window, prompt, location, updateY = True):
    """
    Prompts the user and requests an input

    Parameters:
        window (Window): The window to display to
        prompt (string): The string to prrompt the user with
        location: The starting y-coord
    """
    guess =  window.input_string(prompt, *location)
    if updateY: location[1] += window.get_font_height()
    return guess

def main():
    """
    Main function that runs the game
    """

    # Init
    window = create_window()
    location = [0, 0]
    attempts_left = 4

    display_header(window, location, attempts_left)
    password = display_password_list(window, location)

    guess = get_guesses(window, password, location, attempts_left)

    end_game(window, guess, password)


def create_window():
    """
    Creates the window for the game
    Return: 
        window
    """
    window = uagame.Window("Hacking", 600, 500)

    # Window Style Formatting
    window.set_font_name('couriernew')
    window.set_font_size(18)
    window.set_font_color('green')
    window.set_bg_color('black')
    return window

def display_header(window, location, attempts_left):
    """
    Displays the header

    Parameters:
        window (Window): Window to display to
        location (location): Starting Y-coord
    """
    header = [
        "DEBUG MODE",
        str(attempts_left) + " ATTEMPT(S) LEFT",
        ""
    ]

    for line in header:
        display_line(window, line, location)

def display_password_list(window, location):
    """
    Displays the entire password list

    Parameters:
        window (Window): The window to display to
        location (int): Starting y-coord

    Return:
        (string): The selected password
    """

    # Print Pass List
    passwordList = [
        'PROVIDE',
        'SETTING',
        'CANTINA',
        'CUTTING',
        'HUNTERS',
        'SURVIVE',
        'HEARING',
        'HUNTING',
        'REALIZE',
        'NOTHING',
        'OVERLAP',
        'FINDING',
        'PUTTING'
    ]

    for password in passwordList:
        display_line(window, password, location)

    display_line(window, "", location)

    # Select password from the list
    return passwordList[7] # Selects Hunting

def get_guesses(window, password, location, attempts_left):
    """
    Gets the user's guesses

    Parameters:
        window (Window): The window to display to
        password (string): The correct password
        location (int): Starting y-coord
        attempts_left (int): Number of attempts left

    Return:
        (boolean) Whether the user was succesful or not.
    """
    guess = ""

    while guess != password and attempts_left > 0:
        guess = prompt_user(window, 'ENTER PASSWORD >', location)
        check_warning(window, attempts_left)
        attempts_left -= 1
        display_header(window, [0, 0], attempts_left)

    return guess

def check_warning(window, attempts_left):
    """
    Creates warning code if attempts left is 1
    
    Parameters:
        window (Window): The window to display t
        attempts_left (int): Number of attempts left
    """
    if attempts_left == 1:
        warning = "*** LOCKOUT WARNING ***"
        warningX = window.get_width() - window.get_string_width(warning)
        warningY = window.get_height() - window.get_font_height()
        window.draw_string(warning, warningX, warningY)
    

def display_outcome(window, outcome, location):
    """
    Displays outcome

    Parameters:
        window (Window): Window to display at
        outcome (list): Outcome Lines to display
        location: Starting Y-coord
    """

    for line in outcome:
        if line == "":
            display_line(window, line, location)
            continue
        xOffset = getCenteredStringX(window, line)
        location[0] = xOffset
        display_line(window, line, location)

def end_game(window, guess, password):

    if guess == 'HUNTING':
        outcomeLine2 = "EXITING DEBUG MODE"
        outcomeLine3 = "LOGIN SUCCESSFUL - WELCOME BACK"

    else:
        outcomeLine2 = "LOGIN FAILURE - TERMINAL LOCKED"
        outcomeLine3 = "PLEASE CONTACT AN ADMINISTRATOR"

    outcome = [
        guess,
        "",
        outcomeLine2,
        "",
        outcomeLine3,
        ""
    ]

    location = [0, (window.get_height() - window.get_font_height() * 7) // 2]
    window.clear()

    display_outcome(window, outcome, location)

    exitString = "PRESS ENTER TO EXIT"
    xOffset = getCenteredStringX(window, exitString)
    location[0] = xOffset
    prompt_user(window, exitString, location)

    window.close()

if __name__ == "__main__":
    main()