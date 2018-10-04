# Read input
m, n = [int(i) for i in input().split()]

# Solve
output = 0

for i in range(0, n):
    used, capacity = map(int, input().split())
    if (capacity - used) >= m:
        output += 1

# Output
print(output)