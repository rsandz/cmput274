# A Fibonacci Sequence Calculator
# ===============================
# Now with les RECURSION!

def fib(n):
    """
    Calculates fibonacci squence with n terms
    Param:
        (int) n - Num terms in sequence
    Return:
        (list) Fib seq
    """
    seq = []
    for i in range(n):
        if len(seq) == 0:
            seq.append(i)
        elif len(seq) == 1:
            seq.append(i)
        else:
            seq.append(seq[-1] + seq[-2])

    return seq


if __name__ == '__main__':
    # Run when in called from CLI
    for i in fib(109090909090000):
        print(i)