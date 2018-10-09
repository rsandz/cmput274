def getNextSeq(buses):
    seq = []
    while True:
        num = buses.pop()
        seq.append(num)
        if len(buses) > 0 and (num + 1) == buses[-1]:
            continue
        elif len(seq) > 2:
            return("{}-{}".format(min(seq), max(seq)))
        elif len(seq) == 2:
            return("{} {}".format(seq[0], seq[1]))
        else:
            return seq[0]


# put your solution here
numBus = input()
buses = sorted([int(i) for i in input().split()], reverse = True)

output = []
while len(buses) != 0:
    output.append(getNextSeq(buses))


# Strigify the output
output = [str(i) for i in output]
print(" ".join(output))