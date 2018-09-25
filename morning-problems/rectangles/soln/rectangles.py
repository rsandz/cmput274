# Read in the input
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# Solve the problem

# Look at x

x = [x1, x2, x3]
x4 = None
for elem in x:
    countX = x.count(elem)
    if countX > 1:
        continue
    x4 = elem

y = [y1, y2, y3]
y4 = None
for elem in y:
    countY = y.count(elem)
    if countY > 1:
        continue
    y4 = elem

# Output the result

print("{} {}".format(x4, y4))