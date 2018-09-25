Debug = 2

# TargetWords = ["help","get","911","call","feeling"]
TargetWords = ["help","get","911"]
TargetLabel = ["#gethelp"]

# Dictionaries
FeaturesTarget = {}
FeaturesNot = {}

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


def count_features(label,wordList):
    if label in TargetLabel:
        for w in wordList:
            if w in FeaturesTarget:
                FeaturesTarget[w] += 1
            else:
                FeaturesTarget[w] = 1
    else:
        for w in wordList:
            if w in FeaturesNot:
                FeaturesNot[w] += 1
            else:
                FeaturesNot[w] = 1


def features_stats():
    print( "Features Target: ", FeaturesTarget )
    print()
    print()
    print( "Features Not   : ", FeaturesNot )

    print()
    print()

# https://stackoverflow.com/questions/20944483/python-3-sort-a-dict-by-its-values
# By SzieberthAdam, edited Oct 27 '17 at 16:46, answered Jan 6 '14 at 11:11
    print( "Features Target: ")
    print([(k, FeaturesTarget[k]) for k in sorted(FeaturesTarget, key=FeaturesTarget.get, reverse=True)])
    print()
    print()
    print( "Features Not   : ")
    print([(k, FeaturesNot[k]) for k in sorted(FeaturesNot, key=FeaturesNot.get, reverse=True)])



# Process single line of input
def check_line(inLine):
    global TP,FP,TN,FN
    foundIt = False
    label = inLine.split()[0]
    wordList = inLine.split()[1:]

    count_features(label,wordList)

    for w in TargetWords:
        if w in wordList:
            # Positive
            foundIt = True
            if verbose():
                if label in TargetLabel:
                    print("TP: (%10s) %s" % (w,inLine))
                else:
                    print("FP: (%10s) %s" % (w,inLine))

            if label in TargetLabel:
                TP += 1
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


def confusion_matrix(doKey=False):
    print("%10s | %13s" % ("Predict","Label"))
    print("-----------+----------------------")
    print("%10s | %10s %10s" % (" ",TargetLabel[0],"not"))
    print("%10s | %10d %10d" % (TargetLabel[0],TP,FP))
    if doKey:
        print("%10s | %10s %10s" % ("","TP   ","FP   "))
    print("%10s | %10d %10d" % ("not",FN,TN))
    if doKey:
        print("%10s | %10s %10s" % ("","FN   ","TN   "))

# Process input, then output statistics
#	"Extreme" example of avoiding global variables
# https://en.wikipedia.org/wiki/Precision_and_recall
def main():
    foundCount,totalCount = process_input(0,0)

    if debug():
        print("Target Words: ", TargetWords)
        print("TP+FP count %d.  Total lines %d." % (foundCount,totalCount))
        print("TP %d, TN %d, FP %d, FN %d" % (TP,TN,FP,FN))
        precision = float(TP) / ( TP + FP )
        recall = float(TP) / ( TP + FN )
	# Total +-label = TP + FN
        print("Precision %f, Recall %f" % (precision,recall))
        confusion_matrix(True)
        features_stats()


if __name__ == "__main__":
    main()
