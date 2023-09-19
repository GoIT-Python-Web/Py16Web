class MySQLDatabase:
    def connect(self):
        pass

    def disconnect(self):
        pass


class Application:
    def __init__(self):
        self.database = MySQLDatabase()

    def start(self):
        self.database.connect()
