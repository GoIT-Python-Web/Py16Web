from abc import ABC, abstractmethod


class Bird(ABC):
    @abstractmethod
    def move(self):
        pass


class Ostrich(Bird):
    def move(self):
        return "I can run"


class Sparrow(Bird):
    def move(self):
        return "I can fly"
