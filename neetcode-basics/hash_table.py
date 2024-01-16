# HASH TABLE DATA STRUCTURE (Programiz)

hashTable = [[],] * 10

def checkPrime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2, n//2):
        if n % i == 0:
            return 0

    
    return 1

def getPrime(n):
    if n % 2 == 0:
        n = n + 1