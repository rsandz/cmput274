# =========================
#  Word Splitter
# =========================

while True:
    try:
        wordList = input()
    except EOFError:
        break

    for word in wordList.split():
        print(word)
