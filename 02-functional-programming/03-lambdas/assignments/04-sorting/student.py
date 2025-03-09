sort_by_age = lambda people: sorted(people, key=lambda person: person.age)
sort_by_decreasing_age = lambda people: sorted(people, key=lambda person: person.age, reverse=True)
sort_by_name = lambda people: sorted(people, key=lambda person: person.name)
sort_by_name_then_age = lambda people: sorted(people, key=lambda person: (person.name, person.age))
sort_by_name_then_decreasing_age = lambda people: sorted(sort_by_decreasing_age(people), key=lambda person: person.name)
# sort_by_name_then_decreasing_age = lambda people: sorted(sort_by_name(people), key=lambda person: person.age, reverse=True)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


people = [            Person('John', 18),
            Person('Sarah', 19),
            Person('Peter', 19),
            Person('John', 20),
            Person('Kim', 17),
            Person('Kim', 18),
            Person('Kim', 19),]


people = [
    Person(name="Alice", age=30),
    Person(name="Bob", age=25),
    Person(name="Alice", age=20),
    Person(name="Charlie", age=25)
]


sorted_people = sort_by_name_then_decreasing_age(people)
# sorted_people = sort_by_decreasing_age(people)

for person in sorted_people:
    print(person.name, person.age)