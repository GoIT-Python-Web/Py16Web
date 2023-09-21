from dataclasses import dataclass


class Singleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]


@dataclass
class Settings(metaclass=Singleton):
    db: str = "MySQL"
    port: int = 3306


class NewSettings(Settings):
    pass


if __name__ == '__main__':
    connect = Settings()
    connect_two = Settings()
    t = NewSettings()
    print(connect_two.port)
    connect.port = 5432
    print(connect_two.port)
    print(t.port)
