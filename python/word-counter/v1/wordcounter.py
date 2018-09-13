#=======================
#  Word Counter
#=======================
#  September 06, 2018
#  CMPUT 274

# Init
theCount = 0
cFlag = True

#Functions
def safeInput(msg = ''):
    try:
        userInput = input(msg)    
        return (userInput, True)
    except EOFError:
        return("", False)
    

while cFlag:
    # Ask for input from standard input
    [userInput, cFlag] = safeInput('') # The function safeInput is called the "callsite"
    if (not cFlag):
        break
    
    # Count Frequency, ignoring case
    userInput = userInput.lower()
    if userInput == 'the':
        theCount = theCount + 1

print("""
Result
======
Word: {}
Count: {}
""".format(userInput, theCount))