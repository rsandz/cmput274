#=====================================
# Hacking
#=====================================
# Version 1
#
# Hacking is a terminal based password
# guessing game
#

# Print Header
print('DEBUG MODE')
print('1 ATTEMPT(S) LEFT')
print('')

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
    print(password)

print('')

#User Input

userInput = input('Enter password >')

print('LOGIN FAILURE - TERMINAL LOCKED\n')
print('PLEASE CONTACT AN ADMINISTRATOR\n')


input('PRESS ENTER TO EXIT')