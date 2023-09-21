import datetime


class Event:
    _observers = []  # Слухачі

    # { "event1": [], "event2": []} більш імовірна структура для слухачів

    def register(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unregister(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, event, data=None):
        for observer in self._observers:
            observer(event, data)


def logger(event, data):  # observer
    print(event, data)


class FileLogger:  # observer
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, event, data):
        with open(self.filename, "a", encoding="utf-8") as fd:
            fd.write(f"{datetime.datetime.now()}: [{event}] = {data}\n")


if __name__ == '__main__':
    event = Event()
    event.register(logger)
    fl = FileLogger('logs.txt')
    event.register(fl)

    event.notify('PULS', 65)
    event.notify('PULS', 120)
    event.notify('Ups', "Sometime it happens")
    event.unregister(fl)
    event.notify('PULS', 0)
    event.notify('PULS', 0)
