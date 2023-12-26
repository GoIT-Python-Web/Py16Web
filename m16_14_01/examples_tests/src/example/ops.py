import asyncio


def add(a, b):
    return a + b


def sub(a, b):
    return a-b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


async def async_add(a, b):
    await asyncio.sleep(1)
    return a + b
