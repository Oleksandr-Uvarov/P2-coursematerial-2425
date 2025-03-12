# def take_while(xs, condition):
#     for i in range(len(xs)):
#         if condition(xs[i]) == False:
#             return (xs[0:i], xs[i:])
#     return (xs, [])

def take_while(xs, condition):
    first = []
    second = []
    for item in xs:
        if condition(item):
            first.append(item)
        else:
            second.append(xs[len(first):])
            return (first, second)
    
    return (xs, [])




print(take_while([1, 2, 3, 4, 5], lambda x: x != 3))