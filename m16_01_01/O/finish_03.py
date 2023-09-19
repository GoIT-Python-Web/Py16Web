from abc import ABC, abstractmethod


class Discount(ABC):
    @abstractmethod
    def apply(self, price):
        pass


class SummerDiscount(Discount):
    def apply(self, price):
        return price * 0.9


class BlackFridayDiscount(Discount):
    def apply(self, price):
        return price * 0.7
