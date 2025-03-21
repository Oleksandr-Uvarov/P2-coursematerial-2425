def findMaximum(lst):
    if len(lst) == 0:
        raise IndexError
    maximum = lst[0]
    
    if len(lst) == 1:
        return maximum

    if maximum < findMaximum(lst[1:]):
        return findMaximum(lst[1:])
    return maximum
    

print(findMaximum([1, 2, 3, 4]))
print(findMaximum([3, 2, 4, 1, 5]))
print(findMaximum([3, 2, 4, 6, 5]))