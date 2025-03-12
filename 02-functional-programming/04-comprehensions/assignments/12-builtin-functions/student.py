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

def is_increasing(ns):
    return all(True if ns[i] <= ns[i+1] else False for i in range(len(ns) - 1))

def count_matching(xs, ys):
    return len([xs[i] for i in range(min(len(xs), len(ys))) if xs[i] == ys[i]])

def weighted_sum(ns, weights):
    return sum([ns[i] * weights[i] for i in range(min(len(ns), len(weights)))])

def alternating_caps(string):
    new_string = ""

    for character in (string[i].upper() if i % 2 == 0 else string[i].lower() for i in range(len(string))):
        new_string += character

    return new_string

def find_repeated_words(sentence):
    words = sentence.split()
    words = [word[:-1] if word[-1] in [".", ",", " "] else word for word in words]
    words = [word.lower() for word in words]

    return {words[i] for i in range(len(words) - 1) if words[i] == words[i+1]}

    # repeated_words = set()
    # for i in range(len(words) - 1):
    #     if words[i].lower() == words[i+1].lower():
    #         repeated_words.add(words[i].lower())

    # return repeated_words
    
# some fire code

# lst = ['3', '3','3','32','31','3','23','3','3','33']
# mapping = {"3": True}
# lst_2 = [mapping.get(e, False) for e in lst]
# print(lst_2)

# print(is_prime(3))

# print([number for number in range(0, 1)])

print(find_repeated_words("This sentence has has repeated words. Words."))