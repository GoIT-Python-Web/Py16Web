from functools import reduce

numbers = [1, 14, 6, 19, 34, 22]


def other(a):
    print(a)
    return a


def sum_numbers(numbers):
    other('!!!!!!! Test !!!!!!!!!')
    return reduce(lambda x, y: x + y, numbers)  #


if __name__ == '__main__':
    result = sum_numbers(numbers)
    print(result)
