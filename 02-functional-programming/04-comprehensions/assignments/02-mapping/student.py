def titles(movies):
    return [movie.title for movie in movies]

def titles_and_years(movies):
    return [(movie.title, movie.year) for movie in movies]

def titles_and_actor_counts(movies):
    return [(movie.title, len(movie.actors)) for movie in movies]

def reverse_words(sentence):
    def reverse(word):
        reversed_word = ""
        for i in range(len(word) -1, -1, -1):
            reversed_word += word[i]
        return reversed_word
    
    words = sentence.split(" ")
    reversed_words = [reverse(word) for word in words]

    reversed_sentence = ""

    for word in reversed_words:
        reversed_sentence += word.join(" ")
        reversed_sentence += " "

    reversed_sentence = reversed_sentence[:-1]
    return reversed_sentence

    # short solution reversed_sentence = ' '.join([word[::-1] for word in sentence.split()])

test = "fefw"

def testing(word):
    return [word[i] for i in range(len(word)-1, -1, -1)]
print(testing(test))

print(reverse_words(""))
print(reverse_words("hello"))
print(reverse_words("hello world"))
print(reverse_words("This is a test"))
