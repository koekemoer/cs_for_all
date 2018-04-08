def collatz(n):
    if n % 2 == 0:
        return n/2
    return 3*n + 1

# Recursion
# def collatz(n):
#     if n % 2 == 0:
#         n = n//2
#     else:
#         n = n*3 + 1
#     # print(n)
#     if (n == 1):
#         return n
#     return collatz(n)
    
print(collatz(7))