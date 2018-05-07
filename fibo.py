def fib(n):
  a, b = 0, 1
  
  for i in range(n):
    a, b = b, a + b
    
  return a
  
def productFib(prod):
  currentVal = 0
  i = 0
  f1 = f2 = 0
  
  while currentVal < prod:
    f1 = fib(i)
    f2 = fib(i + 1)
    currentVal = f1 * f2
    i += 1
    
  return [f1, f2, True] if currentVal == prod else [f1, f2, False]
