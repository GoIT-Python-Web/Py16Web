def bubble_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    numbers = [34, 5, 23, 1, 14]
    r = bubble_sort(numbers)
    print(numbers)
