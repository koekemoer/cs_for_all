def square(x):
    return x**2

def quartic(x):
    return x**4

def derivative(f, h):
    '''Returns a new function that is the approximation of
    the derivative of f with respect to h.'''

    return lambda x: (f(x + h) - f(x)) / h

def kthDerivative(f, h, k):
    '''returns a new function that is the approxamation of the
    kth derivative of f with respect to h.'''
    if k == 1:
        return derivative(f, h)
    else:
        return derivative(kthDerivative(f, h, k-1), h)


g = kthDerivative(quartic, 0.0001, 3)
print(g(10))

# g = derivative(square, 0.0001)
# print(g(10))
# # print(g)
# h = derivative(g, 0.0001)
# print(h(10))



# h = derivative(square, 2)
# print(h(10))
