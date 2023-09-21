from enum import Enum
from abc import ABC, abstractmethod


class OperationType(Enum):
    SUM = "summation"
    MUL = "multiplication"


class Operation(ABC):

    @abstractmethod
    def operation(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Adder(Operation):
    def __init__(self, data: list[int]):
        self.data = data

    def operation(self):
        return sum(self.data)

    def info(self):
        return OperationType.SUM.value


class Multiplier(Operation):
    def __init__(self, data: list[int]):
        self.data = data

    def operation(self):
        mul = 1
        for el in self.data:
            mul *= el
        return mul

    def info(self):
        return OperationType.MUL.value


class Factory(ABC):
    @abstractmethod
    def create_operation(self) -> Operation:
        pass

    def make_operation(self) -> Operation:
        return self.create_operation()


class SumFactory(Factory):
    def __init__(self, data):
        self.data = data

    def create_operation(self) -> Operation:
        return Adder(self.data)


class MulFactory(Factory):
    def __init__(self, data):
        self.data = data

    def create_operation(self) -> Operation:
        return Multiplier(self.data)


def calculation(factory: Factory):
    operator = factory.make_operation()
    result = operator.operation()
    return result, operator.info()


if __name__ == '__main__':
    data = [23, 12, 34, 56, 21, 11]

    print(calculation(SumFactory(data)))

    print(calculation(MulFactory(data)))
