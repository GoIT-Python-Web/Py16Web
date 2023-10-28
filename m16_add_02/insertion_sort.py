def insertion_sort(arr: list) -> list:
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp
    return arr


if __name__ == '__main__':
    numbers = [34, 5, 23, 1, 14]
    r = insertion_sort(numbers)
    print(numbers)

