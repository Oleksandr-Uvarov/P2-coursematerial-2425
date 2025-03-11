from util import Card

def genres(movies):
    return {genre for movie in movies for genre in movie.genres}

def actors(movies):
    return {actor for movie in movies for actor in movie.actors}

def repeat_consecutive(xs, n):
    return [x for x in xs for i in range(n)]

def repeat_alternating(xs, n):
    # lists = [xs for i in range(n)]
    # return [x for lst in lists for x in lst]
    return [x for i in range(n) for x in xs]


def cards(values, suits):
    return {Card(value, suit) for value in values for suit in suits}

