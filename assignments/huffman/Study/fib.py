# Modified from
# https://www.programiz.com/python-programming/examples/fibonacci-recursion
# Python program to display the Fibonacci sequence up to n-th term using recursive functions
VERBOSE = False

# Very inefficient way to compute Fibonacci
def recur_fibo(n):
   """Recursive function to
   print Fibonacci sequence"""
   if VERBOSE: print( "  Inside Fib(%3d)" % (n))
   if n <= 1:
       # Base case
       if VERBOSE: print( "  Base case, return (%3d)" % (n))
       return n
   else:
       # Recursive case
       if VERBOSE: print( "\tCall Fib: %3d, %3d" % ((n-1),(n-2)))
       l = recur_fibo(n-1)
       r = recur_fibo(n-2)
       return(l + r)
       # return(recur_fibo(n-1) + recur_fibo(n-2))

# Change this value for a different result
nterms = 50

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
   nterms = int(input("How many terms? "))
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
