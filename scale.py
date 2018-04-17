def scale(n):
    '''Takes a number 'n' as argument and returns a function that multiplies its argument by 'n'.
       eg: f = Scale(42).  Where f is a function and can now receive a number as argument and will multiply that number by 42...
           f(2) = 84'''
    # return lambda x: n*x
    def multiply(x):
        return n*x
    return multiply

f = scale(10)

print(f(9))
print(f(8))
print(f(7))
print(f(6))
print(f(5))
print(f(4))
print(f(3))
print(f(2))
print(f(1))