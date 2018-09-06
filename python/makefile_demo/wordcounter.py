#=======================
#  Word Counter
#=======================
#  September 06, 2018
#  CMPUT 274

# Init
theCount = 0

#Functions
def safeInput(msg):
    try:
        userInput = input(msg)    
        return userInput
    except EOFError:
        return False  
    

while True:
    # Ask for input from standard input
    userInput = safeInput('Enter your word: ')
    if (not safeInput):
        break
    
    # Count Frequency, ignoring case
    userInput = userInput.lower()
    if userInput == 'the':
        theCount = theCount + 1
        
    willContinue = safeInput('Enter more Words? ')
    if not willContinue or willContinue == 'n' or willContinue == 'no':
        break

print("""
Result
======
Word: {}
Count: {}
""".format(userInput, theCount))
