# ===================================================
# Exercise 3: Word Frequency
# ===================================================
# Name: Ryan Sandoval
# ID: 1529017
# Course: CMPUT 274, FALL 2018

import sys

# Debug Flag
DEBUG = False


def main():
    """
    Main Function for running the program
    """
    # Init
    # ====

    # File to analyze from Command line Argument
    if isInputValid():
        fileName = sys.argv[1]
    else:
        sys.exit(1)

    # Analyze the file
    # ================

    words = getWordsInFile(fileName)
    totalWords = len(words)
    wordAmounts = getWordCounts(words)

    # Write Output
    # ============
    outFileName = fileName + ".out"
    outputTable(outFileName, wordAmounts, totalWords)

    if DEBUG:
        print("Words: {}".format(words))
        print("Amount List: {}".format(wordAmounts))


def isInputValid():
    """
    Checks if the Command Line Argument input is valid, as per requirements
    of the assignment.
    Prints validation errors and correct usage if input is not valid

    Return:
        (boolean) True if input is valid. False otherwise.
    """

    exitReason = ""
    usageString = "Usage: {} <File-to-Analyze>".format(sys.argv[0])

    # Check for input amount
    if len(sys.argv) == 2:
        return True
    elif len(sys.argv) > 2:
        exitReason = "Invalid Usage: Too many command line arguments"
    elif len(sys.argv) < 2:
        exitReason = "Invalid Usage: Too few command line arguments"

    print(exitReason)
    print(usageString)

    if DEBUG:
        print("Command Line Args Found: {}".format(len(sys.argv)))
    return False


def getWordsInFile(fileName):
    """
    Reads the file and returns a list of all words in it.
    Also automatically closes file after read

    Parameters:
        fileName (string): File to read

    Return:
        (list) Words in list format
    """
    with open(fileName, 'r') as f:
        lines = f.readlines()

    words = []
    for line in lines:
        words.extend(line.split())

    return words


def getWordCounts(wordList):
    """
    Counts the occurence of each word in a word List

    Parameters:
        wordList (list): The list of words to analyze

    Return:
        (dict) Dictionary containing word as key and
               its amount in wordList as value
    """

    # Get a Unique Words List
    uniqueWords = []

    for word in wordList:
        if word not in uniqueWords:
            uniqueWords.append(word)

    # Count Word Amount
    wordAmounts = {word: wordList.count(word) for word in uniqueWords}

    return wordAmounts


def outputTable(fileName, wordAmounts, totalWords, sort=True):
    """
    Outputs a table to a file as required by the assignment.
    Format is "word count frquency"

    Parameters:
        fileName (string): The name of the file to output to
        wordAmounts (dict): A dictionary with the word as a
                            key and amount as value
        totalWords (int): Total words in the file to analyze
        sort (boolean): Whether to output table sorted in lexographic order.

    Return:
        Void
    """

    # Get the list (wordOrder) dictating order to display words in file
    if sort:
        wordOrder = sorted(wordAmounts)
    else:
        wordOrder = [word for word in wordAmounts]

    # Write to file
    with open(fileName, "w") as f:
        for word in wordOrder:
            amount = wordAmounts[word]

            # Calculate Freq to 3 decimals
            freq = round(amount / totalWords, 3)

            f.write("{} {} {}\n".format(word, amount, freq))


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to
    # this exercise, so you should call your code from here.
    main()
