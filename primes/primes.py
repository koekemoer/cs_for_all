import sys
import math

sys.setrecursionlimit(20000)
def _divisors(n, low, high):
    '''returns True is n has a divisor in the range from low to high'''
    if low > high:
        return False
    elif n % low == 0:
        return True
    else:
        return _divisors(n, low+1, high)

def isPrime(n):
    '''returns True if n is prime'''
    # if _divisors(n, 2, n-1):
    if _divisors(n, 2, math.sqrt(n)):
        return False
    else:
        return True

def _reverseNum(n):
    s = str(n)
    if (s == ''):
        return ''
    else:
        firstSymbol = s[0]
        return _reverseNum(s[1:]) + firstSymbol

# NOT EFFECTIVE
def isEmirp(n):
    if str(n) != _reverseNum(n):
        return isPrime(int(_reverseNum(n)))

def listPrimes(n, limit):
    '''returns a list of prime numbers between n and limit'''
    return (primeSieve(range(n, limit)))

def _sift(toRemove, numList):
    '''takes a number, toRemove, and a list of numbers, numList.
    Returns a list of numbers that is not multiples of toRemove'''
    return list(filter(lambda x: x % toRemove != 0, numList))

def primeSieve(numList):
    '''returns a list of prime numbers out of the numList provided'''
    if numList == []:
        return []
    elif numList[0] <= 1:
        return primeSieve(numList[1:])
    else:
        prime = numList[0];
        return [prime] + primeSieve(_sift(prime, numList))

# NOT DONE
def emirpSieve(numList): 
    # numList = primeSieve(numList)
    return list(filter(isEmirp, numList))

def primeTwins(numList):
    '''returns a list of the Prime Twins in the given numList'''
    numList = primeSieve(numList)
    i = 0
    twinList = []
    while i < (len(numList) - 1):
        x = numList[i]
        if numList[i+1] == x + 2:
            twin = [numList[i], numList[i+1]]
            twinList.append(twin)
        i += 1
    return twinList

def primeTriplets(numList):
    '''returns a list of the Prime Triplets in the given numList'''
    numList = primeSieve(numList)
    i = 0
    tripList = []
    while i < (len(numList) - 2):
        x = numList[i]
        if numList[i+1] == x + 2 or numList[i+1] == x + 4:
            if numList[i+2] == x + 6:
                triplet = [numList[i], numList[i+1], numList[i+2]]
                tripList.append(triplet)
        i += 1
    return tripList

def primeQuads(numList):
    '''returns a list of the Prime Quadruplets in the given numList'''
    numList = primeSieve(numList)
    i = 0
    quadList = []
    while i < (len(numList) - 3):
        x = numList[i]
        if numList[i+1] == x + 2:
            if numList[i+2] == x + 6:
                if numList[i+3] == x + 8:
                    quad = [numList[i], numList[i+1], numList[i+2], numList[i+3]]
                    quadList.append(quad)
        i += 1
    return quadList

primeList = primeSieve(range(1, 1000))
# print(primeList)
print(emirpSieve(primeList))