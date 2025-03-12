def group_movies_by_year(movies):
    return {movie.year: [m.title for m in movies if m.year == movie.year] for movie in movies}
