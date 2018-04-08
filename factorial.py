def factorial(n):
    if (n == 1):
        return 1
    else:
        result = n * factorial(n - 1)
        return result

print(factorial(2))
print(factorial(1))
print(factorial(4))
print(factorial(7))