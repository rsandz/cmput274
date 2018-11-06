import re
# Add your code here
string = str(input())

digPattern = re.compile(r"[0-9]")
string = re.sub(digPattern, "", string)

matchLengths = []

for pos in range(len(string)):
    count = 0
    movString = string[pos:]
    for index, char in enumerate(movString):
        if string[index] == char:
            count += 1
            continue
        break
    
    matchLengths.append(str(count))


print(" ".join(matchLengths))