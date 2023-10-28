def shell_sort(arr: list) -> list:
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and temp < arr[j - gap]:
                arr[j] = arr[j - gap]
                j = j - gap
            arr[j] = temp
        gap = gap // 2
    return arr


if __name__ == '__main__':
    numbers = [34, 5, 23, 1, 14]
    r = shell_sort(numbers)
    print(r)

