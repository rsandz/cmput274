# Read in the input
a,b,c = map(int, input().split())

def checkSame(a, b, c):
    """
    Checks if all numbers are same
    """

    if a == b and b == c:
        return True

def checkSim(a, b, c):
    """
    Check is a number occurs twice in array
    """

    nums = [a, b, c]
    for num in nums:
        if (nums.count(num) > 1):
            return True

    # Number does not occur twice... 
    # Must mean that my dish sucked :(
    return False

# Results
# =======

if (checkSame(a, b, c)):
    print('same')
elif (checkSim(a, b, c)):
    print('similar')
else:
    print('distinct')



