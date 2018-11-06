import sys

sourceBadLetters = list("vkjxqz")

for line in sys.stdin:
    badLetters = {char: 0 for char in sourceBadLetters}
    if line == "\n":
        continue

    for char in line:
        char = char.lower()
        if char in badLetters:
            badLetters[char] |= 1
    if sum(badLetters.values()) > 4:
        print("BAD")
    else:
        print("OK")

    
