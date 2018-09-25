# Next feature: import random
import string

Debug = 2

TargetWords = ["help", "get", "stuck", "911", "dizzy"]

# Predicate:  Debug
def debug():
    if Debug > 0:
        return True
    else:
        return False


# Predicate:  Verbose Debug
def verbose():
    if Debug > 1:
        return True
    else:
        return False


# Read single line from standard in and handle EOF
def safe_input(prompt):
    try:
        wordInput = input(prompt)
        return(wordInput, True)
    except EOFError:
        return("", False)


# Process single line of input
def check_line(inLine):
    foundIt = False

    label = inLine.split()[0]
    wordList = inLine.split()[1:]

    for w in TargetWords:
        if w in wordList:
            foundIt = True
            if verbose():
                print("Found: ({}) {} {}".format(w, label, " ".join(wordList)))
            break

    return(foundIt)


# Process all input
def process_input(foundCount, totalCount):
    cFlag = True
    while cFlag:
        inLine, cFlag = safe_input("")
        if not cFlag:
            break
        totalCount += 1
        foundIt = check_line(inLine)

        if (foundIt):
            foundCount += 1

    return(foundCount, totalCount)


# Process input, then output statistics
#	"Extreme" example of avoiding global variables
def main():
    foundCount,totalCount = process_input(0,0)

    if debug():
        print("Target Features: ", TargetWords)
        print("Get-help count %d.  Ok count %d.  Total Input Count %d." %
              (foundCount, totalCount - foundCount, totalCount))

if __name__ == "__main__":
    main()
