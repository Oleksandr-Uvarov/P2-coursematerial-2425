from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def make_noise(self):
        print("make noise")
        ...


class Giraffe(Animal):
    def make_noise(self):
        super().make_noise()
        print("giraffe makes noise")


giraffe = Giraffe()

giraffe.make_noise()