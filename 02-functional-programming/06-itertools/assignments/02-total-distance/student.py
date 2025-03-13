from itertools import pairwise

def total_distance(path, distance):
    return sum([distance(cities[0], cities[1]) for cities in list(pairwise(path))])

