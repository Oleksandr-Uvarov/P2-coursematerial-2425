def title_to_director(movies):
    return {movie.title: movie.director for movie in movies}

def director_to_titles(movies):
    return {movie.director: [movie_.title for movie_ in movies if movie_.director == movie.director] for movie in movies}