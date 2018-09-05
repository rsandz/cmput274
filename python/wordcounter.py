#===========================
# Counting Word Frequency
#===========================
# September 04, 2018

#Init
theCount = 0

# Getting Input
userInput = input('Enter your Text: ')
if userInput.lower() == 'the':
    theCount = theCount + 1
    
# Format the Input
result = """
Result
======
Word: {}
Count: {}
""".format(userInput, theCount)
print(result)

