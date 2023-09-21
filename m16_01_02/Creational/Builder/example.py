from abc import ABC, abstractmethod


class Car:
    def __init__(self):
        self.parts = {}

    def add(self, key: str, value: str):
        self.parts[key] = value

    def show(self):
        print("Автомобіль складається з:")
        for key, value in self.parts.items():
            print(f"{key}: {value}")


class Builder(ABC):
    @abstractmethod
    def build_wheels(self):
        pass

    @abstractmethod
    def build_doors(self):
        pass

    @abstractmethod
    def build_engine(self):
        pass

    @abstractmethod
    def get_result(self):
        pass


class GasBuilder(Builder):

    def __init__(self):
        self.car = Car()

    def build_wheels(self):
        self.car.add("Колеса", "4")

    def build_doors(self):
        self.car.add("Двері", "4")

    def build_engine(self):
        self.car.add("Двигун", "V1.6")

    def get_result(self) -> Car:
        return self.car


class ElectricCarBuilder(Builder):

    def __init__(self):
        self.car = Car()

    def build_wheels(self):
        self.car.add("Колеса", "4")

    def build_doors(self):
        self.car.add("Двері", "2")

    def build_engine(self):
        self.car.add("Двигун", "200КВ")

    def get_result(self) -> Car:
        return self.car


class Director:
    def __init__(self, builder: Builder):
        self.builder = builder

    def constructor(self):
        self.builder.build_wheels()
        self.builder.build_doors()
        self.builder.build_engine()


if __name__ == '__main__':
    auto_builder = GasBuilder()
    director = Director(auto_builder)
    director.constructor()
    auto = auto_builder.get_result()
    auto.show()

    auto_builder = ElectricCarBuilder()
    director = Director(auto_builder)
    director.constructor()
    auto = auto_builder.get_result()
    auto.show()