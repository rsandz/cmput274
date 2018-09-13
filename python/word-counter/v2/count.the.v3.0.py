import string

TargetWords = ['the', 'The']
UniqueWords = []
UniqueFirstLetter = []

Debug = False


# User-defined function to do input and handle EOF
def safe_input(prompt):
    try:
        wordInput = input(prompt)
        return(wordInput, True)
    except EOFError:
        return("", False)


def main():
    theCount = 0
    skipCount = 0
    cFlag = True
    while cFlag:
        word, cFlag = safe_input("")
        if not cFlag:
            break
        if (word in TargetWords):
            theCount = theCount + 1
            if Debug:
                print("Count %d. %s" % (theCount, word))
        else:
            if Debug:
                print("Skip '%s' " % (word))
            skipCount = skipCount + 1

        # Do other Statistics gathering
        if (word not in UniqueWords):
            UniqueWords.append(word)
        if (word[0].isalpha() and word[0].lower() not in UniqueFirstLetter):
            UniqueFirstLetter.append(word[0].lower())
        
    print("Found count %d.  Skipped %d.  All words %d."
        % (theCount, skipCount, theCount + skipCount))
    print("Unique Word Count: {}. {}".format(len(UniqueWords), UniqueWords[0:5]))
    UniqueFirstLetter.sort()
    print("Unique First Letters: {}.".format("".join(UniqueFirstLetter)))
    print("Alphabet            : {}.".format(string.ascii_lowercase))


if __name__ == "__main__":
    main()
