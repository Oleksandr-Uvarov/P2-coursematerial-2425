class Person:
    def __init__(self, age):
        self.__age = age

    def double_age(self):
        return self.__age * 2
    

person = Person(19)
double = person.double_age()
print(double)
print(double)