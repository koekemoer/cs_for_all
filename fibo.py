import math as m

def fibValue(n):
'''Using sqrt method'''
  phi = (1 + m.sqrt(5))/2
  res = round((phi**n)/(m.sqrt(5)))
  return res

def fib(n):
  a, b = 0, 1
  
  for i in range(n):
    a, b = b, a + b
    
  return a
  
def productFibLongAssWay(prod):
  currentVal = 0
  i = 0
  f1 = f2 = 0
  
  while currentVal < prod:
    f1 = fib(i)
    f2 = fib(i + 1)
    currentVal = f1 * f2
    i += 1
    
  return [f1, f2, True] if currentVal == prod else [f1, f2, False]

def productFib(prod):
  f1, f2 = 0, 1
  while prod > f1 * f2:
    f1, f2 = f2, f1 + f2
  return [f1, f2, f1*f2 == prod]
