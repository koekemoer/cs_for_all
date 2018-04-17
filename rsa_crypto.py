import primes.prime_functions as primes
import random
from functools import *

def inverse(e, m):
    '''returns the inverse of e mod m'''
    return list(filter(lambda d: e*d % m == 1, range(1, m)))[0]

def makeEncoderDecoder():
    '''Returns two functions: An RSA encyption function and 
    an RSA decryption function'''

    # Choose 2 primes
    p, q = random.sample(primes.listPrimes(2, 20), 2)
    n = p*q
    m = (p-1)*(q-1)
    print("Max number that can be encrypted is: ", n-1)

    # Choose a random prime for e
    e = random.choice(primes.primeSieve(range(2, m)))
    if e % m == 0:
        print('PLease try again')
        return
    else:
        d = inverse(e, m)
        # print(d)
        encoder = lambda x: (x**e) % n # encryption function
        decoder = lambda y: (y**d) % n # decryption function
        return [encoder, decoder]

makeEncoderDecoder()