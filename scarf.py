#--------------------------------------------------
# Change these variables to design your own scarf!
# Add a comment describing what each variable does.
#--------------------------------------------------

#Scarf Colours
colours = ['#','|', ':']

#How long each color
colour_length = 10

#Scarf Length
pattern_length = 25

#Scarf width
pattern_width = 10

#------------------------------------------------
# Don't change anything below this line!
#------------------------------------------------

print("Here is your scarf:\n")
for pos in range(int(pattern_width * pattern_length)):
    print( colours[ int((pos)/colour_length) % len(colours)], end="")
    if (pos % pattern_width) == pattern_width-1:
        print("")