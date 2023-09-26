import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(funcName)5s - %(message)s")


def baz1000000011(num: int):
    foo = 100
    result = foo + num
    logging.debug(f"result: {result}")
    return result


if __name__ == '__main__':
    baz1000000011(500)
