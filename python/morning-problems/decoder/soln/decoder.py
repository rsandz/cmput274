# Read in the input
dictlen = int(input())

# Read dict
dict = {}
for _ in range(dictlen):
    dictEntry = input().split()
    dict[dictEntry[0]] = dictEntry[1]

# Read code
code = list(input())
code.reverse() # So we can use pop
output = ""

# Decode
while len(code) > 0:
    subcode = code.pop() # Subsection of code
    while subcode not in dict:
        subcode += code.pop()
    # Found Match
    output += dict[subcode] + " "

#Strip whitespace for presentation
output = output.strip()
print(output)
