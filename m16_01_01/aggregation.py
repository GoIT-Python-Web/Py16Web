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
    def __init__(self, nickname, age, owner: Owner):
        super().__init__(nickname, age)
        self.owner = owner

    def say(self):
        return f"{self.nickname} say meow!"


if __name__ == '__main__':
    cat = Cat('Simon', 6, Owner('Yurii', '0509112323'))