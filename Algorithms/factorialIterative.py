#factorialIterative.py
#CMCDonnell 18-09-23

# An iterative solution to factorial
def factorial(n):
    
    answer = 1
    for i in range(n, 1, -1): 
        answer = answer * i
    
    return answer

# Test the function 
x = 5
print("%d! = %d" %(x, factorial(5)))
