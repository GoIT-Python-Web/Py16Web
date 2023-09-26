from typing import Callable


def foo():
    return "Hello world"


def call_function(func: Callable[[], str]) -> int:
    return len(func())


Number = int | float  # Union[str, float]


def calc(x: Number, y: Number) -> Number:
    return x + y


def call_function1(
    func: Callable[[Number, Number], Number], a: Number, b: Number
) -> Number:
    return func(a, b)


def call_function2(func: Callable[..., str], *args):
    return func(*args)


if __name__ == "__main__":
    print(call_function(foo))
    print(call_function1(calc, 5, 5))
