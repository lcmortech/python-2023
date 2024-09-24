# calculating the factorial of a number
# factorials only involve positive integers

# iterative method
def iterative_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i # fact = fact * i
    return fact

print(iterative_factorial(5))

# recursive method