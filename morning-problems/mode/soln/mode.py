words = input().split()

# words is now a list of all strings in the input
# wordCount = {word: words.count(word) for word in words}

maxCount = 0
for word, count in wordCount.items():
    if count > maxCount:
        maxCount = count
uniqueWords = []

for word in words:
    if word not in words:
        uniqueWords.append(word)
sortedWords = sorted(uniqueWords)

for word in sortedWords:
    if maxCount == wordCount[word]:
        print(word)
# finish the problem!

# sortedWords = sorted(words)

# unique = []
# [unique.append(word) for word in sortedWords if word not in unique]

# maxCount = 0
# out = []
# for word in unique:
#     if sortedWords.count(word) > maxCount:
#         out = [word]
#         maxCount = sortedWords.count(word)

#     elif sortedWords.count(word) == maxCount:
#         out.append(word)
    
#     else:
#         continue

# print("\n".join(out))


