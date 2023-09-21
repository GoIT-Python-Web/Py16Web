class Greeting:
    def __init__(self, username):
        self.username = username

    def greet(self):
        return f"Hello {self.username}"


class GreetingDecorator:
    def __init__(self, wrapper: Greeting):
        self.wrapper = wrapper

    def greet(self):
        base_greet = self.wrapper.greet()
        return base_greet.upper()


if __name__ == '__main__':
    message = GreetingDecorator(Greeting("Oleksandr"))
    print(message.greet())
    