# Code by Paul Lu
import sys
# Command-line argumets:
# https://www.tutorialspoint.com/python3/python_command_line_arguments.htm
import getopt

# Default parameters
Debug = 2
TrainingDataFile = "training.data"
ConfigFile = "config.help"
AutoFeatures = False
Pipeline = False
SupportThreshold = 1
DoAddOneSmoothing = 1

TargetWords = []
TargetLabel = []

# Dictionaries
FeaturesTarget = {}	# Count of features in target label
FeaturesNot = {}	# Count of features in Neg label

# pNB
PNBPosFeatures = {}
PNBNegFeatures = {}
PNBPosCount = 0
PNBNegCount = 0
PNBPosFeaturesCount = 0
PNBNegFeaturesCount = 0


TP = 0
FP = 0
TN = 0
FN = 0

# Metrics for how many decisions were made by the classifier, vs. forced
ForcedOnlyPos = 0
ForcedOnlyNeg = 0
NBDecide = 0

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


# Predicate:  Verbose Debug
def superverbose():
    if not Pipeline and Debug > 2:
        return True
    else:
        return False


# Predicate:  Add-one smoothing
def smoothing():
    if DoAddOneSmoothing > 0:
        return True
    else:
        return False


def reset_stats():
    global TP,FP,TN,FN,FeaturesTarget,FeaturesNot
    global ForcedOnlyPos,ForcedOnlyNeg,NBDecide

    TP = 0
    FP = 0
    TN = 0
    FN = 0
    FeaturesTarget = {}
    FeaturesNot = {}

    # Metrics for how many decisions were made by the classifier, vs. forced
    ForcedOnlyPos = 0
    ForcedOnlyNeg = 0
    NBDecide = 0


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
        # FIXME Catch specific exceptions
        if debug():
            print( "File open failed: %s" % (filename) )
        return("", False)


# One of many ways to handle this
def read_whole_file( fd ):
    try:
        lines = fd.readlines()
        fd.close()
        # Remove newline at end for all
	# https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html
        newL = [l.strip() for l in lines]
        # print(newL)
        return(newL)
    except:
        print("File read failed")
        sys.exit( -1 )
    

def count_features_in_list(label,wordList):
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
    global FeaturesTarget,FeaturesNot
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


def choose_features_by_support():
    '''
    Choose features based on counts (in FeaturesTarget) being greater than
    threshold (in SupportThreshold)
    '''
    global FeaturesTarget

# https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html
# https://stackoverflow.com/questions/20944483/python-3-sort-a-dict-by-its-values
# By SzieberthAdam, edited Oct 27 '17 at 16:46, answered Jan 6 '14 at 11:11

    labelFeatures = [(k, FeaturesTarget[k]) for k in sorted(FeaturesTarget, key=FeaturesTarget.get, reverse=True)]

    ##### Features, support
    i = 1  # Initialize
    for (f,k) in labelFeatures:
        if k == SupportThreshold:	# Find first k == SupportThreshold
            i = labelFeatures.index((f,k))
            break
    assert( i >= 1 )


    # Count > SupportThreshold for a feature
    return(labelFeatures[0:i-1])



# Process single line of input
def target_words_check_line(inLine):
    global TP,FP,TN,FN
    foundIt = False
    label = inLine.split()[0]
    wordList = inLine.split()[1:]

    count_features_in_list(label,wordList)

    for w in TargetWords:
        if w in wordList:
            # Positive
            foundIt = True
            if verbose():
                if label in TargetLabel:
                    print("TW TP: (%10s) %s" % (w,inLine))
                else:
                    print("TW FP: (%10s) %s" % (w,inLine))

            if label in TargetLabel:
                TP += 1
            else:
                FP += 1

            break

    if not foundIt:
        if label not in TargetLabel:
            TN += 1
            if verbose():
                    print("TW TN: (%10s) %s" % (label,inLine))
        else:
            FN += 1
            if verbose():
                    print("TW FN: (%10s) %s" % (label,inLine))

    return(foundIt)


# Train pNB, single line of input
def train_pseudo_naive_bayes_line(inLine):
    global PNBPosCount,PNBNegCount,PNBPosFeaturesCount,PNBNegFeaturesCount
    ok = True
    label = inLine.split()[0]
    featureList = inLine.split()[1:]

    # Positive case
    if label in TargetLabel:
        PNBPosCount += 1
        PNBPosFeaturesCount += len(featureList)
        for w in featureList:
            if w in PNBPosFeatures:
                PNBPosFeatures[w] += 1
            else:
                # Add-one smoothing
                # https://en.wikipedia.org/wiki/Additive_smoothing
                PNBPosFeatures[w] = 2
                if smoothing() and (w not in PNBNegFeatures):
                    PNBNegFeatures[w] = 1
    # Negative
    else:
        PNBNegCount += 1
        PNBNegFeaturesCount += len(featureList)
        for w in featureList:
            if w in PNBNegFeatures:
                PNBNegFeatures[w] += 1
            else:
                # Add-one smoothing
                # https://en.wikipedia.org/wiki/Additive_smoothing
                PNBNegFeatures[w] = 2
                if smoothing() and (w not in PNBPosFeatures):
                    PNBPosFeatures[w] = 1

    return(ok)


# Classify pNB, single line of input
def classify_pseudo_naive_bayes_line(inLine):
    global PNBPosCount,PNBNegCount,PNBPosFeaturesCount,PNBNegFeaturesCount
    global TP,FP,TN,FN
    global TargetLabel
    global ForcedOnlyPos,ForcedOnlyNeg,NBDecide

    ok = True
    label = inLine.split()[0]
    featureList = inLine.split()[1:]

    PNBTotalData = PNBPosCount + PNBNegCount
    posNum = float(PNBPosCount) / PNBTotalData
    negNum = float(PNBNegCount) / PNBTotalData

    # Positive case
    if verbose():
        print()
        print( "Start Pos: ", posNum, label, featureList)
    for w in featureList:
        if w in PNBPosFeatures:
            posNum *= float(PNBPosFeatures[w]) / PNBPosFeaturesCount
            if superverbose():
                print(w, posNum, PNBPosFeatures[w], PNBPosFeaturesCount)
            if w not in PNBNegFeatures:
                negNum = 0.0
                # Feature only in Pos cases
                if verbose():
                    print(w, " only in pos ***")
        else:
            pass
    if verbose():
        print( "End Pos: ", posNum )
        if posNum == 0.0:
            print( "*** Zero Pos")


    # Negative case
    if verbose():
        print( "Start Neg: ", negNum, label, featureList)
    for w in featureList:
        if w in PNBNegFeatures:
            negNum *= float(PNBNegFeatures[w]) / PNBNegFeaturesCount
            if superverbose():
                print(w, negNum, PNBNegFeatures[w], PNBNegFeaturesCount)
            if w not in PNBPosFeatures:
                # Feature only in Neg cases
                posNum = 0.0
                if verbose():
                    print(w, " only in neg ***")
        else:
            pass

    if verbose():
        print( "End Neg: ", negNum )
        if negNum == 0.0:
            print( "*** Zero Neg")

    # Make the prediction
    if (posNum >= negNum):
        predClass = TargetLabel[0]
    else:
        predClass = "Neg"


    # Metrics for how many decisions were made by the classifier, vs. forced
    if (posNum == 0.0):
        ForcedOnlyNeg += 1

    if (negNum == 0.0):
        ForcedOnlyPos += 1

    if (negNum != 0.0 and posNum != 0.0):
        NBDecide += 1

    # **** Do the metrics
    if predClass in TargetLabel:
        if predClass == label:
            TP += 1
            if verbose():
                print("TP: (%10s/%g/%g,%10s) %s" % (predClass,posNum,negNum,label,featureList))
        else:
            FP += 1
            if verbose():
                print("FLAG FP: (%10s/%g/%g,%10s) %s" % (predClass,posNum,negNum,label,featureList))
    else:
        if label not in TargetLabel:
            TN += 1
            if verbose():
                print("TN: (%10s/%g/%g,%10s) %s" % (predClass,posNum,negNum,label,featureList))
        else:
            FN += 1
            if verbose():
                print("FLAG FN: (%10s/%g/%g,%10s) %s" % (predClass,posNum,negNum,label,featureList))

    return((predClass,posNum,negNum))


# Process one line of input
def process_line(inLine,foundCount,totalCount):
    global TargetWords,TargetLabel

    foundIt = False
    # Check for parameters embedded in training data file
    param = inLine.split()[0]
    if param == "%":  # Comment.  Skip.
        pass
    elif param == "%pos-features":
        TargetWords = inLine.split()[1:]
        if debug():
            print("TargetWords Hardcoded (%d): %s" % (len(TargetWords),TargetWords))
    elif param == "%pos-label":
        TargetLabel = inLine.split()[1:]
        if debug():
            print(TargetLabel)
    else:
        totalCount += 1
        foundIt = target_words_check_line(inLine)
        if(foundIt):
            foundCount += 1

    return(foundCount,totalCount,foundIt)


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

        foundCount,totalCount,ok = process_line(inLine,foundCount,totalCount)
        # Do nothing with ok, for now
    return(foundCount,totalCount)


# Process all input, from file
def process_input_file(allLines,foundCount,totalCount):
    for l in allLines:
        foundCount,totalCount,ok = process_line(l,foundCount,totalCount)
        # Do nothing with ok, for now
    return(foundCount,totalCount)


# train pNB all input, from list
def train_pseudo_naive_bayes_all(allLines):
    global PNBPosFeatures,PNBNegFeatures
    global PNBPosCount,PNBNegCount,PNBPosFeaturesCount,PNBNegFeaturesCount

    PNBPosFeatures = {}
    PNBNegFeatures = {}
    PNBPosCount = 0
    PNBNegCount = 0
    PNBPosFeaturesCount = 0
    PNBNegFeaturesCount = 0

    TP = 0
    FP = 0
    TN = 0
    FN = 0

    ok = True
    for l in allLines:
        ok = train_pseudo_naive_bayes_line(l)

    if superverbose():
        print("XXX pfset: ",list(PNBPosFeatures.keys()),len(list(PNBPosFeatures.keys())))

    return(ok)


# classify pNB all input, from list
def classify_pseudo_naive_bayes_all(allLines):
    global PNBPosCount,PNBNegCount,PNBPosFeaturesCount,PNBNegFeaturesCount
    global ForcedOnlyPos,ForcedOnlyNeg,NBDecide

    predAllLines = []
    for l in allLines:
        predClass,posNum,negNum = classify_pseudo_naive_bayes_line(l)
        predAllLines.append((predClass,posNum,negNum))

    print("NB Decide: ",NBDecide,"Forced Positive:",ForcedOnlyPos,"Forced Negative: ",ForcedOnlyNeg)
    return(predAllLines)


def confusion_matrix(header="",doKey=False):
    print(header)
    print("%10s | %13s" % ("Predict","Label"))
    print("-----------+----------------------")
    print("%10s | %10s %10s" % (" ",TargetLabel[0],"not"))
    print("%10s | %10d %10d" % (TargetLabel[0],TP,FP))
    if doKey:
        print("%10s | %10s %10s" % ("","TP   ","FP   "))
    print("%10s | %10d %10d" % ("not",FN,TN))
    if doKey:
        print("%10s | %10s %10s" % ("","FN   ","TN   "))


def usage(argv):
    print("Usage: %s -t <training data file> -q <query>" % (argv[0]))


def hardcodedTargetWordClassify(foundCount,totalCount,fromFile,trainingData):
    global TargetWords

    print("EXP ** Classify by Hardcoded Words")
    print("Target Words (%d): " % len(TargetWords), TargetWords)
    print("TP+FP count %d.  Total lines %d." % (foundCount,totalCount))
    print("TP %d, TN %d, FP %d, FN %d" % (TP,TN,FP,FN))
    precision = float(TP) / ( TP + FP )
    recall = float(TP) / ( TP + FN )
    print("Precision %f, Recall %f" % (precision,recall))


def learnedTargetWordClassify(foundCount,totalCount,fromFile,trainingData):
    global TargetWords

    # Simple learning
    print("EXP ** Classify by Words Found in Training")

    if fromFile:
        cf = choose_features_by_support()
        if superverbose():
            print(cf)
        TargetWords = sorted([ f for (f,k) in cf])
        if superverbose():
            print()
            print()
        print("Learned Targets (%d): %s" % (len(TargetWords),(" ".join(TargetWords))))
        justData = [ l for l in trainingData if l[0] != "%"]
        # print(justData)

        reset_stats()
        foundCount,totalCount = process_input_file(justData,0,0)
        if debug():
            print("Target Words (%d): " % len(TargetWords), TargetWords)
            print("TP+FP count %d.  Total lines %d." % (foundCount,totalCount))
            print("TP %d, TN %d, FP %d, FN %d" % (TP,TN,FP,FN))
            precision = float(TP) / ( TP + FP )
            recall = float(TP) / ( TP + FN )
	    # Total +-label = TP + FN
            print("Precision %f, Recall %f" % (precision,recall))


def binaryNBClassify(foundCount,totalCount,fromFile,trainingData):
    global FeaturesTarget

    print("EXP ** Classify by Binary Naive Bayes Classifier")
    # Pseudo-Naive Bayes
    if fromFile:
        featuresPositive = FeaturesTarget.copy()
        posFeatures = [(k, FeaturesTarget[k]) for k in sorted(FeaturesTarget, key=FeaturesTarget.get, reverse=True)]
        # numPosFeatures = 0
        # for (k,v) in posFeatures:
        #     numPosFeatures += v

        featuresNegative = FeaturesNot.copy()
        negFeatures = [(k, FeaturesNot[k]) for k in sorted(FeaturesNot, key=FeaturesNot.get, reverse=True)]
        # numNegFeatures = 0
        # for (k,v) in negFeatures:
        #     numNegFeatures += v

        if debug():
            print("************* Number Positive Features %d, Negative Features %d" % (len(posFeatures),len(negFeatures)))


        justData = [ l for l in trainingData if l[0] != "%"]
        train_pseudo_naive_bayes_all(justData)
        if superverbose():
            print( "Pos Train Count: ", PNBPosCount,"Neg Train Count: ",PNBNegCount)
            print( "Pos Features Count: ", PNBPosFeaturesCount, "Neg Features Count: ",PNBNegFeaturesCount)
            print( "Positive Features: ", PNBPosFeatures )
            print()
            print( "Negative Features: ", PNBNegFeatures )

        reset_stats()
        allDataPred = classify_pseudo_naive_bayes_all(justData)
        if debug():
            print()
            print()
            print("TP+FP count %d.  Total lines %d." % (foundCount,totalCount))
            print("TP %d, TN %d, FP %d, FN %d" % (TP,TN,FP,FN))
            precision = float(TP) / ( TP + FP )
            recall = float(TP) / ( TP + FN )
	    # Total +-label = TP + FN
            print("Precision %f, Recall %f" % (precision,recall))


# ************************************************
# Process input, then output statistics
# https://en.wikipedia.org/wiki/Precision_and_recall
def main():
    global TargetWords
    global ForcedOnlyPos,ForcedOnlyNeg,NBDecide

# https://docs.python.org/3/howto/argparse.html
# https://docs.python.org/3/library/getopt.html
# https://www.tutorialspoint.com/python3/python_command_line_arguments.htm

    print("Command Line Arguments: ", str(sys.argv))
    try:
        opts,args = getopt.getopt(sys.argv[1:], "ht:q:")
    except:
        usage(sys.argv)
        sys.exit(2)
    for o,a in opts:
        if o == "-t":
            print("CLA Training Data File:  %s" % (a))
            # Do something more
        elif o == "-q":
            print("CLA Q:  %s" % (a))
            # Do something more
        elif o == "-h":
            usage(sys.argv)


    # Process configuration file, if any
    fd,ok = open_file(ConfigFile)
    if ok:
        configLines = read_whole_file(fd)
        process_config(configLines)

    # Read in whole training data file
    fd,fromFile = open_file(TrainingDataFile)
    if fromFile:
        if debug():
            print("Training data from:  %s" % (TrainingDataFile))
        trainingData = read_whole_file(fd)
        foundCount,totalCount = process_input_file(trainingData,0,0)
    else:
        if debug():
            print("Training data from STANDARD IN")
        foundCount,totalCount = process_input_stdin(0,0)

    # Experiment 1
    print()
    hardcodedTargetWordClassify(foundCount,totalCount,fromFile,trainingData)
    confusion_matrix("EXP ** Classify by Hardcoded Words")
    if verbose():
        features_stats()

    # Experiment 2
    print()
    learnedTargetWordClassify(foundCount,totalCount,fromFile,trainingData)
    confusion_matrix("EXP ** Classify by Words Found in Training")
    if verbose():
        features_stats()

    # Experiment 3
    print()
    binaryNBClassify(foundCount,totalCount,fromFile,trainingData)
    confusion_matrix("EXP ** Classify by Binary Naive Bayes Classifier")


# ************************************************
if __name__ == "__main__":
    main()
