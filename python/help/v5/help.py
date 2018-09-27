import sys

# Default parameters
Debug = 2
TrainingDataFile = "training.data"
ConfigFile = "config.help"
AutoFeatures = True
Pipeline = False
SupportThreshold = 1

# TargetWords = ["help","get","911"]
TargetWords = []
# TargetLabel = ["#gethelp"]
TargetLabel = []

# Dictionaries
FeaturesTarget = {}
FeaturesNot = {}

TP = 0
FP = 0
TN = 0
FN = 0

# Predicate:  Debug
def debug():
    if not Pipeline and Debug > 0:
        return True
    else:
        return False


# Predicate:  Verbose Debug
def verbose():
    if not Pipeline and Debug > 1:
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


def open_file( filename ):
    try:
        f = open( filename, "r" )
        return(f, True)
    except:
        if debug():
            print( "File open failed: %s" % (filename) )
        return("", False)


# One of many ways to handle this
def read_whole_file( fd ):
    try:
        lines = fd.readlines() # Let the OS handle performance when reading GB of data!
        fd.close()
        # print(lines)
        # Remove newline at end for all
	# https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html
        newL = [l.strip() for l in lines]
        # print(newL)
        return(newL)
    except:
        print("File read failed")
        sys.exit( -1 )
    

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
# https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html
# https://stackoverflow.com/questions/20944483/python-3-sort-a-dict-by-its-values
# By SzieberthAdam, edited Oct 27 '17 at 16:46, answered Jan 6 '14 at 11:11
    labelFeatures = [(k, FeaturesTarget[k]) for k in sorted(FeaturesTarget, key=FeaturesTarget.get, reverse=True)]
    notFeatures = [(k, FeaturesNot[k]) for k in sorted(FeaturesNot, key=FeaturesNot.get, reverse=True)]

    ##### Features, support
    i = 1  # Initialize
    for (f,k) in labelFeatures:
        if k == SupportThreshold:	# Find first k == SupportThreshold
            i = labelFeatures.index((f,k))
            break
    # print(labelFeatures[i])
    assert( i >= 1 )

    # Count > SupportThreshold for a feature
    print("Key Features: ", labelFeatures[0:i-1])

    # Count <= SupportThreshold for a feature
    # http://www.diveintopython.net/power_of_introspection/filtering_lists.html
    tt = [k for (k,j) in labelFeatures[i:] if j <= SupportThreshold]
    print("Other: ", ",".join(tt))

    ##### NOT Features
    print()
    print()
    i = 1  # Initialize
    for (f,k) in notFeatures:
        if k == SupportThreshold:	# Find first k == SupportThreshold
            i = notFeatures.index((f,k))
            break
    # print(labelFeatures[i])
    assert( i >= 1 )

    # Count > SupportThreshold for a feature
    print("NOT Features: ",notFeatures[0:i-1])

    # Count <= SupportThreshold for a feature
    # http://www.diveintopython.net/power_of_introspection/filtering_lists.html
    tt = [k for (k,j) in notFeatures[i:] if j <= SupportThreshold]
    print("Other: ", ",".join(tt))


    # print()
    # print("Features Target: ")
    # print(labelFeatures)
    # print()
    # print()
    # print("Features Not: ")
    # print(notFeatures)



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


# Process one line of input
def process_line(inLine,foundCount,totalCount):
    global TargetWords,TargetLabel

    # Check for parameters embedded in training data file
    param = inLine.split()[0]
    if param == "%":  # Comment.  Skip.
        pass
    elif param == "%pos-features":
        TargetWords = inLine.split()[1:]
        if debug():
            print(TargetWords)
    elif param == "%pos-label":
        TargetLabel = inLine.split()[1:]
        if debug():
            print(TargetLabel)
    else:
        totalCount += 1
        foundIt = check_line(inLine)
        if(foundIt):
            foundCount += 1

    return(foundCount,totalCount)


# Process one line of input
def process_line_config(inLine):
    global Debug,TrainingDataFile
    param = inLine.strip().split()
    if param[0] == "%":  # Comment.  Skip.
        pass
    elif param[0] == "Debug":
        Debug = int(param[1])
        if verbose():
            print("Debug:  %d" % (Debug))
    elif param[0] == "TrainingDataFile":
        TrainingDataFile = str(param[1])
        if verbose():
            print("TrainingDataFile:  %s" % (TrainingDataFile))


# Process all input
def process_config(lines):
    for l in lines:
        process_line_config(l)



# Process all input, from standard in
def process_input_stdin(foundCount,totalCount):
    cFlag = True
    while cFlag:
        inLine, cFlag = safe_input("")
        if not cFlag:
            break

        foundCount,totalCount = process_line(inLine,foundCount,totalCount)
    return(foundCount,totalCount)


# Process all input, from file
def process_input_file(allLines,foundCount,totalCount):
    for l in allLines:
        foundCount,totalCount = process_line(l,foundCount,totalCount)
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
# https://en.wikipedia.org/wiki/Precision_and_recall
def main():
    fd,ok = open_file(ConfigFile)
    if ok:
        configLines = read_whole_file(fd)
        process_config(configLines)

    fd,ok = open_file(TrainingDataFile)
    if ok:
        if debug():
            print("Training data from:  %s" % (TrainingDataFile))
        trainingData = read_whole_file(fd)
        foundCount,totalCount = process_input_file(trainingData,0,0)
    else:
        if debug():
            print("Training data from STANDARD IN")
        foundCount,totalCount = process_input_stdin(0,0)

    if debug():
        print("Target Words: ", TargetWords)
        print("TP+FP count %d.  Total lines %d." % (foundCount,totalCount))
        print("TP %d, TN %d, FP %d, FN %d" % (TP,TN,FP,FN))
        precision = float(TP) / ( TP + FP )
        recall = float(TP) / ( TP + FN )
	# Total +-label = TP + FN
        print("Precision %f, Recall %f" % (precision,recall))
        confusion_matrix()
        features_stats()


if __name__ == "__main__":
    main()
