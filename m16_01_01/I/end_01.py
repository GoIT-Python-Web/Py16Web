from abc import ABC, abstractmethod


class Workable(ABC):

    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):

    @abstractmethod
    def eat(self):
        pass


class Man(Workable, Eatable):

    def work(self):
        return "Working hard."

    def eat(self):
        return "Eating lunch."


class Robot(Workable):

    def work(self):
        return "Working automatically."

