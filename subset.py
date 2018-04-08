def subset(capacity, items):
    '''Given a suitcase capacity and a list of items
       consisting of positive numbers, returns a number
       indicating the largest sum that can be made from a
       subset of the items without exceeding the capacity.'''
    
    if capacity <= 0 or len(items) == 0:
        print(1)
        return 0
    elif items[0] > capacity:
        print(2)        
        return subset(capacity, items[1:])
    else:
        print(3)        
        loseIt = subset(capacity, items[1:])
        print(4)        
        useIt = items[0] + subset(capacity - items[0], items[1:])
        print(5)
        return max(loseIt, useIt)
    
# print(subset(42, [46, 84, 40, 20, 21, 3]))
print(subset(4, [2, 1]))