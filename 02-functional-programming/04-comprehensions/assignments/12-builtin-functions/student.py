def movie_count(movies, director):
    return len([movie for movie in movies if movie.director == director])

def longest_movie_runtime_with_actor(movies, actor):
    return max([movie.runtime for movie in movies for m_a in movie.actors if m_a == actor])

def has_director_made_genre(movies, director, genre):
    # return len([movie for movie in movies for g in movie.genres if movie.director == director and g == genre]) != 0
    return any([True if movie.director == director and g == genre else False for movie in movies for g in movie.genres])

def is_prime(n):
    if n == 0 or n == 1:
        return False
    return all(False if n % number == 0 else True for number in range(2, n))

    # or messy one-liner
    # return all(False if n in [0, 1] or (number not in [0, 1, n] and n % number == 0) else True for number in range(0, n+1))







# some fire code

# lst = ['3', '3','3','32','31','3','23','3','3','33']
# mapping = {"3": True}
# lst_2 = [mapping.get(e, False) for e in lst]
# print(lst_2)

print(is_prime(3))

# print([number for number in range(0, 1)])