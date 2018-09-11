#========================
# Dice Game for Python
#========================
# Lab 3
# Ryan Sandoval


from random import randint

outcomes =[
    "Do action A",
    "Do action B",
    "Do action C",
    "Do action D",
    "Do action E",
    "Do action F",
]

# generate the pseudo - random number
number = randint (1 ,len(outcomes))

# display the number
print("""
Results
=======
Your Number is {}
Its respective action is: {}
""".format(number, outcomes[number - 1]))
