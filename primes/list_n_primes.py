import is_prime as primes

def list_primes(n):
    '''Lists N number of prime numbers'''
    i, count = 2, 1
    while count <= n:
        if primes.is_prime(i):
            print(count, ':', i)
            count += 1
        i += 1

# list_primes(10)
list_primes(11)