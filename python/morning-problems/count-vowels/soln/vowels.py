# read the input
string = input().lower()

# solve the problem
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for vowel in vowels:
    count += string.count(vowel)


# output the result
print(count)