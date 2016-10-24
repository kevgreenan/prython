import sys
import math

number = input("Enter a number that is the product of two prime numbers: ")
def isPrime(number, lb):
    if number < math.sqrt(lb/2):
        return 0
    if number == 2:
        return 1
    boundary = int(math.floor(math.sqrt(number)))
    for i in range(2, boundary):
        if number % i == 0:
            return 0
    return 1
def findPrime(num):
    sqrnum = math.sqrt(num)
    l=0
    slb = sqrnum
    sub = sqrnum + 1
    lb = slb * slb
    ub = sub * sub
    print("Lowerbound: ", lb, " Upperbound: ", ub)
    array = [0,0,0,0,0,0]
    primes = [0,0,0,0,0,0]
    for i in range(0, 5):
        array[0] = slb + i
        array[1] = slb - i
        array[2] = array[0] * array[1]
        array[3] = sub + i
        array[4] = sub - i
        array[5] = array[3] * array[4]
        for j in range(0, 5):
            if isPrime(array[j], lb):
                if array[1] <= 0 and array[4] <= 0:
                    l = i + 1
                    i = num - 1
                primes.append(int(array[j]))
    primes = list(set(primes))
    primes.sort()
    for i in range(0, len(primes)):
       for j in range(0, len(primes)):
            if primes[i] * primes[j] == num:
                print(primes[i], primes[j])
    print(primes)

# execute
findPrime(number)
