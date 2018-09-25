# Word Chop
# =========
# This will get an input and then
# print all the letters of eac word 
# except for the first and last ones.

stringList = input("Enter String: ").split()
toPrint = ""

for string in stringList:
    if len(string) <= 2:
        toPrint += string + " "
        continue
    toPrint += string[1:-1] + " "

print(toPrint)
