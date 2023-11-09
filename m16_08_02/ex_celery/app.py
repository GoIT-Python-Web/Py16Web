from my_task import add, sub

if __name__ == '__main__':
    result = add.delay(1, 1)
    print(result.id)
    result = sub.delay(5, 3)
    print(result.id)
