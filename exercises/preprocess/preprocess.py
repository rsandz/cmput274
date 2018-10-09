# ===================================================
# Exercise 4: Text Preprocessor
# ===================================================
# Name: Ryan Sandoval
# ID: 1529017
# Course: CMPUT 274, FALL 2018

import re
import sys

# Debug Flag
DEBUG = False

# Stop words - Words removed from preprocessed Text
STOPWORDS = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves",
             "you", "your", "yours", "yourself", "yourselves", "he",
             "him", "his", "himself", "she", "her", "hers", "herself",
             "it", "its", "itself", "they", "them", "their", "theirs",
             "themselves", "what", "which", "who", "whom", "this", "that",
             "these", "those", "am", "is", "are", "was", "were", "be", "been",
             "being", "have", "has", "had", "having", "do", "does", "did",
             "doing", "a", "an", "the", "and", "but", "if", "or", "because",
             "as", "until", "while", "of", "at", "by", "for", "with",
             "about", "against", "between", "into", "through", "during",
             "before", "after", "above", "below", "to", "from", "up", "down",
             "in", "out", "on", "off", "over", "under", "again", "further",
             "then", "once", "here", "there", "when", "where",
             "why", "how", "all", "any", "both", "each", "few", "more",
             "most", "other", "some", "such", "no", "nor", "not", "only",
             "own", "same", "so", "than", "too", "very", "s", "t",
             "can", "will", "just", "don", "should", "now"]


def main():
    """
    Runs the program's main functionality
    """
    # Get mode from command line
    mode = parseCommandArgs()

    # Grab input
    analyte = input().split()

    processedWords = normalizeWordList(analyte, mode)

    # Print processed words in a line
    print(" ".join(processedWords))


def parseCommandArgs():
    """
    Parses then validates the command arguments passed into the program.

    Return:
        (string) - Indicates mode of the preprocessor. None if default mode
    """
    # Init
    programFile = sys.argv[0]
    args = sys.argv[1:]  # Note: Mode Argument has index 0
    validArgs = ["keep-digits", "keep-stops", "keep-symbols"]

    # Usage string: Contains CLI syntax and options
    usage = "Usage: python3 {} <mode>\n<mode> : {}".format(
        programFile,
        ", ".join(validArgs)
        )

    # No args
    if len(args) < 1:
        return None

    # Invalid Number of args
    if len(args) > 1:
        print("Too many command line arguments")
        print(usage)
        sys.exit(1)

    # Check if valid arg
    if args[0] in validArgs:
        return args[0]
    else:
        print("Invalid mode passed")
        print(usage)
        sys.exit(1)


def normalizeWordList(wordList, mode):
    """
    Normalizes a  list containing tokens of a text

    Parameter:
        wordList (list) - text tokens
        mode (string) - Mode for word processing. Can be:
                        "keep-digits" - Keeps digits
                        "keep-stops" - Keep Stop words
                        "keep-symbols" - Keep Non alphanumerics

    Return:
        (list) - processed text
    """
    processedWords = []

    for word in wordList:
        normalizedWord = normalize(word, mode)

        if normalizedWord is not None:
            processedWords.append(normalizedWord)

    return processedWords


def normalize(word, mode):
    """
    Normalizes the word by (in order):
        - Lowercasing it
        - Removing ALL non-alphanumeric characters
        - Remove numbers (Unless word is a number itself)
    Also checks if word is stopword. If so, returns none

    Parameters:
        word (string) - Word to normalize
        mode (string) - Mode for word processing. Can be:
                        "keep-digits" - Keeps digits
                        "keep-stops" - Keep Stop words
                        "keep-symbols" - Keep Non alphanumerics

    Return:
        (string|None) - The normalized word or None if it is a stopword
    """

    # Lower case word
    word = word.lower()

    # Check if stopword
    if mode != "keep-stops" and word in STOPWORDS:
        return None

    if mode != "keep-symbols":
        # Use Regex to remove non-alphanumeric
        symbolPattern = re.compile(r"[^A-Za-z0-9]+")
        word = re.sub(symbolPattern, "", word)

    # Check for numbers 
    if word.isdigit():
        return word

    # Use regex to remove invalid digits
    if mode != "keep-digits":
        digitsPattern = re.compile(r"\d+")
        word = re.sub(digitsPattern, "", word)

    # Word is now processed
    return word


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 preprocess.py". This is directly relevant
    # to this exercise, so you should call your code from here.
    main()
