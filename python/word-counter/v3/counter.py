# Next feature: import random
import string

Debug = 1

TargetWords = ["the","The"]

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
def check_line(word,theCount,skipCount,uWords,uFirstLetter):
    if word in TargetWords:
        theCount = theCount + 1
        if verbose():
            print("Count %d. %s" % (theCount, word))
    else:
        if verbose():
            print("Skip '%s' " % (word))
        skipCount = skipCount + 1

    # Do other statistics gathering
    if word not in uWords:
        uWords.append(word)

    if word[0].isalpha() and (word[0].lower() not in uFirstLetter):
        uFirstLetter.append(word[0].lower())

    return(theCount,skipCount,uWords,uFirstLetter)


# Process all input
def process_input(theCount,skipCount,uWords,uFirstLetter):
    cFlag = True
    while cFlag:
        word, cFlag = safe_input("")
        if not cFlag:
            break
        theCount,skipCount,uniqueWords,uniqueFirstLetter = check_line(word,theCount,skipCount,uWords,uFirstLetter)

    return(theCount,skipCount,uWords,uFirstLetter)


# Process input, then output statistics
#	"Extreme" example of avoiding global variables
def main():
    theCount,skipCount,uniqueWords,uniqueFirstLetter = process_input(0,0,[],[])

    if debug():
        print("Target Words: ", TargetWords)
        print("Found count %d.  Skipped %d.  All words %d." %
              (theCount, skipCount, theCount + skipCount))
        if verbose():
            print(uniqueWords)
        print("Unique word count:  %d." % (len(uniqueWords)), uniqueWords[0:5])
        uniqueFirstLetter.sort()
        print("Found    %s" % "".join(uniqueFirstLetter))
        print("Alphabet %s" % string.ascii_lowercase)


if __name__ == "__main__":
    main()
