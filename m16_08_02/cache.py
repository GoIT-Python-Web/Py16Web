import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def fibonacci(n):  # O(2^n)
    if n <= 1:
        # базовий випадок
        return n
    else:
        # рекурсивний випадок
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(f"Result: {fibonacci(35)}")
