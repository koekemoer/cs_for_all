def digitalRoot(n):
    res = 0
    if n < 10:
        return n
    else:
        for i in str(n):
            res += int(i)
        return digitalRoot(res) 

# print(digitalRoot(42))
# print(digitalRoot(84))
# print(digitalRoot(126))
# print(digitalRoot(168))
# print(digitalRoot(210))
# print(digitalRoot(12345678))
# print(digitalRoot(1234567))
# print(digitalRoot(123456))
# print(digitalRoot(12345))
print(digitalRoot(1))
print(digitalRoot(2))
print(digitalRoot(2**2))
print(digitalRoot(2**3))
print(digitalRoot(2**4))
print(digitalRoot(2**5))
print(digitalRoot(2**6))
print(digitalRoot(2**7))
print(digitalRoot(2**8))
print(digitalRoot(2**9))
print(digitalRoot(2**10))
print(digitalRoot(2**11))