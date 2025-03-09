def genres(movies):
    return {genre for genre in [movie.genres for movie in movies]}

def actors(movies):
    return {actor for actor in {movie.actors for movie in movies}}

