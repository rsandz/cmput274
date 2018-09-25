#=====================================
# Hacking
#=====================================
# Version 2
#
# Hacking is a terminal based password
# guessing game
#

# Imports
import uagame
import time

# Init
window = uagame.Window("Hacking", 600, 500)
lineHeightOffset = 0

def printWindow(msg, x = 0, y = None, delay = 0.3):
    """
    Prints msg to the uagame Window with the proper
    line height offset.

    Arguments:
        msg (string): The message to display
        x (int): pixel offset for x
        y (int): pixel offset for y
        delay (float): Delay between prints

    Return:
        void
    """
    global lineHeightOffset

    if not y:
        y = lineHeightOffset

    window.draw_string(msg, x, y)
    lineHeightOffset += window.get_font_height()
    window.update()
    time.sleep(0.3)

def getCenteredStringX(string):
    """
    Gets X offset needed to center text

    Arguments:
        string (string): String to center

    Return:
        (integer): X Offset for string
    """
    return (window.get_width() - window.get_string_width(string)) // 2

# Window Style Formatting
window.set_font_name('couriernew')
window.set_font_size(18)
window.set_font_color('green')
window.set_bg_color('black')

# Print Header
header = [
    "DEBUG MODE",
    "1 ATTEMPT(S) LEFT",
    ""
]

for line in header:
    printWindow(line)

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
    printWindow(password)

printWindow("")

# User Input
userInput = window.input_string('ENTER PASSWORD >', 0, lineHeightOffset)

# Print Outcome
lineHeightOffset = (window.get_height() - window.get_font_height() * 7) // 2
window.clear()

outcome = [
    userInput,
    "",
    "LOGIN FAILURE - TERMINAL LOCKED",
    "PLEASE CONTACT AN ADMINISTRATOR",
    ""
]

for line in outcome:
    xOffset = getCenteredStringX(line)
    printWindow(line, xOffset)

exitString = "PRESS ENTER TO EXIT"
xOffset = getCenteredStringX(exitString)
window.input_string(exitString, xOffset, lineHeightOffset)

window.close()