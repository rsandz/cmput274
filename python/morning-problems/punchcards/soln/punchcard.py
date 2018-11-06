import sys

# this will read in every line until the end of file
# caution: the newline at the end of a line is not automatically stripped!
lineAcc = ""
for line in sys.stdin:
    # if the line was empty (contains only a newline), what does the problem
    # statement ask you to do?
    if line == "\n":
        print(lineAcc)
        lineAcc = ""
        continue
    # if the line is not empty, it corresponds
    # to some ascii character - do something with it!
    line = line.replace("X", "1")
    line = line.replace(".", "0")

    # Convert to int
    lineVal = int(line, 2)

    lineAcc += chr(lineVal)

