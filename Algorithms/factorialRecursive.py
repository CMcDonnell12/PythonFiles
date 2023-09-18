#factorialRecursive.py
# @CMcDonnell 18-09-2023
# Purpose: A program to demonstrate a recursive computations of factorial
# A recursive solution to factorial
def factorial(n):
    
    if n == 0:
        return 1
    
    return n * factorial(n-1)


# Test the function 
x = 5
print("%d! = %d" %(x, factorial(5)))
