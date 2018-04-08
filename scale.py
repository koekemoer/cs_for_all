def scale(n):
    # return lambda x: n*x
    def multiply(x):
        return n*x
    return multiply

f = scale(42)

print(f(9))
print(f(8))
print(f(7))
print(f(6))
print(f(5))
print(f(4))
print(f(3))
print(f(2))
print(f(1))