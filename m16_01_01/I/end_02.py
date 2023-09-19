from abc import abstractmethod, ABC


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class OldPrinter(Printer):
    def print(self, document):
        # actual print logic
        pass
