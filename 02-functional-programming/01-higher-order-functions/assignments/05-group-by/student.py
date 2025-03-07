def age(person):
    return person.age

def group_by(xs, key_function):
    dictionary = {}
    for element in xs:
        value = key_function(element)
        if dictionary.get(value) == None:
            dictionary[value] = []
        dictionary[value].append(element)

    return dictionary


# group_by([
#     Person(name='John', age=14),
#     Person(name='Marc', age=17),
#     Person(name='Sophie', age=15),
#     Person(name='Chris', age=17),
#     Person(name='Morgan', age=15),
# ], age)