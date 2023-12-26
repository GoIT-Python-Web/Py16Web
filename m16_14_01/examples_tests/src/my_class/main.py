class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"


class CatDog(Cat, Dog):  #
    def info(self):  #
        return f"{self.nickname}-{self.weight}"  #


class DogCat(Dog, Cat):  #
    def info(self):  #
        return f"{self.nickname}-{self.weight}"  #


# MRO