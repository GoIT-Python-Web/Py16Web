def quicksort(arr: list) -> list:
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[n // 2]
    left = [el for el in arr if el < pivot]
    middle = [el for el in arr if el == pivot]
    right = [el for el in arr if el > pivot]

    return quicksort(left) + middle + quicksort(right)


if __name__ == '__main__':
    numbers = [34, 5, 23, 1, 14]
    r = quicksort(numbers)
    print(r)
