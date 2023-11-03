numbers = [1, 3, 5, 7, 9, 11]


def liners_search(arr: list, x):  # O(n)
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


print(liners_search(numbers, 7))
