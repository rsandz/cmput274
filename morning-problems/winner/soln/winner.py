import math

# Read the input
n = int(input())

debug = False
winner = False
turns = 0

while not winner:

    if (n % 3) - 1 == 0:
        n = n - 1

    else:
        n = n - 2

    turns = turns + 1
    
    if n <= 0:
        winner = True
        break
    if debug:
        print(n)
    
    


# Alice if even, Bob if odd
if (turns % 2 == 1):
    print('Alice wins')
else:
    print('Bob wins')


