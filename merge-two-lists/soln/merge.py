# Get the input
list1 = input().split()
list2 = input().split()
output = []

# Solve the problem
maxRange = max([len(list1), len(list2)])

for i in range(maxRange):
    if len(list1) >= (i + 1):
        output.append(list1[i])
    
    if len(list2) >= (i + 1):
        output.append(list2[i])

# Print the result
print(" ".join(output))