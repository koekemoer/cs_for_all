from functools import *

def add(x, y):
    return x + y

def triple(x):
    return 3 * x

def mapReduce(mapFunc, reduceFunc, myList):
    '''Applies mapFunction to myList to
	            construct a new list and then
	            applies reduceFunction to the
	            new list and returns
	            reduceFunction's result.'''
    
    # newList = map(mapFunc, myList)
    # value = reduce(reduceFunc, newList)
    # return value

    return reduce(reduceFunc, map(mapFunc, myList))

# print(mapReduce(triple, add, [1,2,3,4,5,6,7,8]))
# print(mapReduce(triple, add, [1,2,3,4,5,6]))
# print(mapReduce(triple, add, [1,2]))
print(reduce(add, [1,2,3,4,5,6,7,8,9]))
print(reduce(add, [1,2,3,4,5,6,7,8]))
print(reduce(add, [1,2,3,4,5,6,7]))
print(reduce(add, [1,2,3,4,5,6]))
print(reduce(add, [1,2,4,5]))
print(reduce(add, [1,2,3,4]))
print(reduce(add, [1,2,3]))
print(reduce(add, [1,2]))