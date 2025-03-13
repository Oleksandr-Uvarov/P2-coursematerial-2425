from itertools import combinations, permutations, pairwise


# print(list(combinations(range(4), 2)))
# print(list(permutations(range(4), 4)))


def find_shortest_path(distance, city_count):

    temp = list(permutations(range(1, city_count), city_count-1))
    pm = []
    for t in temp:
        t = list(t)
        t.insert(0, 0)
        t.append(0)
        pm.append(t)


    minimal_distance_route = pm[0]
    minimal_distance = 100000

    for p in pm:
        pairs_of_distances = list(pairwise(p))
        total_distance = 0
        for pair in pairs_of_distances:
            total_distance += distance(pair[0], pair[1])
        if total_distance < minimal_distance:
            minimal_distance = total_distance
            minimal_distance_route = p
    
    return minimal_distance_route
        

    
    # for p in pm:
    #     print(list(pairwise(p)))
    #     # distances.append(sum(distance(path[0], path[1]) for path in list(pairwise(p))))
    #     d = {p: sum(distance(path[0], path[1]) for path in list(pairwise(p)))}

    # print(d)
    
    # min_d = 10000
    # min_k = None
    # for key, value in d.items():
    #     if value < min_d:
    #         min_d = value
    #         min_k = key
    
    # return min_k


def distance(a, b):
    return a + b

# print(find_shortest_path(distance, 4))

lst = list(permutations(range(1, 4), 3))
lst_2 = []
for l in lst:
    l = list(l)
    l.insert(0, 0)
    l.append(0)
    lst_2.append(l)


# print(lst_2)
print(find_shortest_path(distance, 4))

# print(list(pairwise([1, 2, 3, 4])))