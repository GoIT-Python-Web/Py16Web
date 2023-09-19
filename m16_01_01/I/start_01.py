from abc import ABC, abstractmethod


class Worker(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Man(Worker):

    def work(self):
        return "Working hard."

    def eat(self):
        return "Eating lunch."


class Robot(Worker):

    def work(self):
        return "Working automatically."

    def eat(self):
        raise Exception("Robots don't eat!")
