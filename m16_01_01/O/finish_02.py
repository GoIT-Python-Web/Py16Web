from abc import ABC, abstractmethod


# class Logger():
#
#     def log(self, message):
#         raise NotImplementedError

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass


class ConsoleLogger(Logger):
    def log(self, message):
        print(message)


class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        with open(self.filename, 'w') as file:
            file.write(message)


