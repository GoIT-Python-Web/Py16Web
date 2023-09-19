from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class MySQLDatabase(Database):
    def connect(self):
        pass

    def disconnect(self):
        pass


class Application:
    def __init__(self, database: Database):
        self.database = database

    def start(self):
        self.database.connect()
