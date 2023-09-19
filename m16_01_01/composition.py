# Композиція коли хозяїн не існує окремо від тварини

class Animal:
    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def get_info(self) -> str:
        return f"It's an animal. His name is {self.nickname} and he's {self.age} years old"


class Owner:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def info(self):
        return f"{self.name}: {self.phone}"


class Cat(Animal):
    pass
