# How the stack works
def demo(x):
    r = f(x + 6) + x
    return r

def f(x):
    r = g(x - 1)
    x = 1
    return r + x

def g(x):
    r = x + 10
    return r

# print (demo(13))
# print (demo(11))
# print (demo(42))
# print (demo(98))