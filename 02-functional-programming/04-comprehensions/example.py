def squares(ns):
    return [n**2 for n in ns]

print(squares([1, 2, 3, 4, 5]))

def select_adults(people):
    return [person for person in people if person.age >= 18]

def select_adult_names(people):
    return [
        person.name
        for person in people
        if person.age >= 18
    ]


def create_dictionary_of_students(students):
    return {student.id: student for student in students}


def first_10_numbers(number_list):
    return [number_list[i] for i in range(10)]

number_list = [1, 2, 1, 2,1, 2,1, 2,1, 2,1, 2,1, 2,1, 2,1, 2,1, 2,1, 2,1, 2,1, 2,1, 2,1, 2,1, 2,1, 2]
print(first_10_numbers(number_list))


# result_list = []

# for x in "abcd":
#     for y in range(4):
#         result_list.append((x, y))

# print(result_list)


result_list = [(x, y) for x in "abcd" for y in range(4)]

print(result_list)


argument = [[3, 6, 22, 32], [8, 11, 27, 37], [32, 35, 51, 61]]
result = []
for lst in argument:
    for element in lst:
        result.append(element)

# or

argument = [[3, 6, 22, 32], [8, 11, 27, 37], [32, 35, 51, 61]]
result = [element for lst in argument for element in lst]



list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
print(list(zip(list1, list2)))

print(list(enumerate(list1)))