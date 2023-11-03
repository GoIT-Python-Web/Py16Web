def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:
        index = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))
        if arr[index] == x:
            return index
        if arr[index] < x:
            low = index + 1
        else:
            high = index - 1

    return -1


arr = [1, 3, 5, 7, 9, 11, 14, 16, 18, 20, 22, 25, 28, 30]
index = interpolation_search(arr, 25)  # 11
print(arr[index])  # 25
