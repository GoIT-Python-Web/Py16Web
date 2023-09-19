from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def start(self):
        pass


class GasEngine(Engine):
    def start(self):
        return "Gas engine started"


class ElectricEngine(Engine):
    def start(self):
        return "Electric engine started"


# Автомобілі
class Car(ABC):
    def __init__(self, engine: Engine):
        self.engine = engine

    @abstractmethod
    def start(self):
        pass


class ElectricCar(Car):
    def start(self):
        return f"Electric car: {self.engine.start()}"


class GasCar(Car):
    def start(self):
        return f"Gas car: {self.engine.start()}"


gas_engine = GasEngine()
el_engine = ElectricEngine()

mazda = GasCar(gas_engine)
tesla = ElectricCar(el_engine)

print(mazda.start())
print(tesla.start())
