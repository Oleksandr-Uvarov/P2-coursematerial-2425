def is_palindrome(string):
    return string == string[::-1]


def indices_of(xs, condition):
    indices = []
    for i in range(len(xs)):
        if condition(xs[i]):
            indices.append(i)

    return indices