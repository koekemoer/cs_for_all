import math

def is_prime(n):
    '''Tests if number given is a prime number'''
    divisor = 2
    prime = True
    # while divisor <= math.sqrt(n):
    while divisor < n:
        if n % divisor == 0:
            prime = False
        divisor += 1
    return prime