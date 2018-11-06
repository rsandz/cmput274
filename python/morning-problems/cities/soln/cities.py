n = int(input())
flights = {}
for i in range(n):
    # now get the two city strings for each of the first n lines
    # Hint: Consider using a dictionary here...
    # replace the pass keyword below with your code
    cityFrom, cityTo = input().split("---")
    flights[cityFrom] = cityTo


# you still have to read in the 2nd part of the input
# which consists of the value q followed by the q query lines

q = int(input())

for i in range(q):
    currentCity = input()
    numFlights = 0
    while True:
        if currentCity == "Edmonton":
            break
        currentCity = flights[currentCity]
        numFlights += 1

    print(numFlights)

# for each query, calculate and print the answer
