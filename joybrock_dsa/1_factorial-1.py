# calculating the factorial of a number
# factorials only involve positive integers

# iterative method
def iterative_factorial(num):
    fact = 1
    for i in range(2, num + 1):
        fact *= i #fact = fact * i
    return fact

print(iterative_factorial(5))

# recursive method
# last in, first out (LIFO)

def recur_factorial(num):
    if num == 1:
        return num
    else:
        fact = recur_factorial(num - 1)
        fact *= num #fact = fact * num

    return fact


    
