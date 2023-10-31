def counting_sort(arr, position):
    size = len(arr)
    output = [0] * size
    count = [0] * 10

    # Рахунок входжень певного розряду
    for i in range(0, size):
        index = arr[i] // position % 10
        t = arr[i]
        count[index] += 1

    for i in range(0, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = arr[i] // position % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]


def radix_sort(arr):
    max_num = max(arr)
    position = 1
    while max_num // position > 0:
        counting_sort(arr, position)
        position *= 10
    return arr


if __name__ == '__main__':
    numbers = [34, 5, 23, 1, 14, 1, 2, 2]
    r = radix_sort(numbers)
    print(numbers)
