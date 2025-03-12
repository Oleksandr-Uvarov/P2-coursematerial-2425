def partition(lst, condition):
    elements_1 = []
    elements_2 = []

    for element in lst:
        if condition(element):
            elements_1.append(element)
        else:
            elements_2.append(element)
        
    return (elements_1, elements_2)

def children_and_adults(people):
    def is_adult(person):
        return person.age >= 18
    
    return partition(people, is_adult)

