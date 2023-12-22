import random
from sympy import isprime


def generate_large_prime():
    while True:
        num = random.randint(10 ** 9, 10 ** 10)
        if isprime(num):
            return num


def is_prime(n, k=5):  # k - кількість ітерацій
    """
    Check if a given number is prime.

    Parameters:
        n (int): The number to be checked for primality.
        k (int, optional): The number of iterations for the primality test. Defaults to 5.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    # Знаходимо r та d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Проводимо k тестів
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# Приклад використання:
n = generate_large_prime()
print(n)
print(is_prime(n))  # поверне False, хоча 561 - псевдопросте число
