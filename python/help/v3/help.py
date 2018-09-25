# Next feature: import random
import string

Debug = 2

TargetWords = ["help","get", "911", "stuck", "dizzy", "lie"]
TargetLabel = ["#gethelp"]

TP = 0
FP = 0
TN = 0
FN = 0

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
        wordInput = input(prompt).strip()
        return(wordInput, True)
    except EOFError:
        return("", False)


# Process single line of input
def check_line(inLine):
    # NOTE: Global vars do not get found automtically in nested functions!!!
    # Always Explicitly acknowledgeand declare `global` vars
    global TP,FP,TN,FN
    # nonlocal TP,FP,TN,FN
    foundIt = False
    label = inLine.split()[0]
    wordList = inLine.split()[1:]
    for w in TargetWords:
        if w in wordList:
            # Positive
            foundIt = True
            if verbose():
                print("Found: (%s) %s" % (w,inLine))

            if label in TargetLabel:
                TP += 1
                if verbose():
                    print("    Match %s" % (label))
            else:
                FP += 1

            break

    if not foundIt:
        if label not in TargetLabel:
            TN += 1
        else:
            FN += 1

    return(foundIt)


# Process all input
def process_input(foundCount,totalCount):
    cFlag = True
    while cFlag:
        inLine, cFlag = safe_input("")
        if not cFlag:
            break

        totalCount += 1
        foundIt = check_line(inLine)
        if(foundIt):
            foundCount += 1

    return(foundCount,totalCount)


# Process input, then output statistics
#	"Extreme" example of avoiding global variables
# https://en.wikipedia.org/wiki/Precision_and_recall
def main():
    foundCount,totalCount = process_input(0,0)

    if debug():
        print("Target Words: ", TargetWords)
        print("Found count %d.  Total lines %d." % (foundCount,totalCount))
        print("TP %d, TN %d, FP %d, FN %d" % (TP,TN,FP,FN))
        precision = float(TP) / ( TP + FP )
        recall = float(TP) / ( TP + FN )
	# Total +-label = TP + FN
        print("Precision %f, Recall %f" % (precision,recall))


if __name__ == "__main__":
    main()
