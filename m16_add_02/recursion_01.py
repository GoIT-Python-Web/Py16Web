from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):  # O(2^n)
    if n <= 1:
        # базовий випадок
        return n
    else:
        # рекурсивний випадок
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memo(n, memo=None):  # O(n)
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        # базовий випадок
        return n
    else:
        # рекурсивний випадок
        value = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
        memo[n] = value
        return value


if __name__ == '__main__':
    result = fibonacci(499)
    print(result)
    result = fibonacci_memo(499)
    print(result)
