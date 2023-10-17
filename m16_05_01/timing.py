from functools import wraps
from time import time


def async_timed(name: str = None):
    if name:
        print(name)

    def wrapper(func):
        @wraps(func)
        async def wrapped(*args, **kwargs):
            start = time()
            try:
                return await func(*args, **kwargs)
            finally:
                print(time() - start)

        return wrapped

    return wrapper


def sync_timed(name: str = None):
    if name:
        print(name)

    def wrapper(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            start = time()
            try:
                return func(*args, **kwargs)
            finally:
                print(time() - start)

        return wrapped

    return wrapper
