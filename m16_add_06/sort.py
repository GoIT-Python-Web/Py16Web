import heapq


def heap_sort_simple(iterable):
    h = iterable[:]
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]


def heap_sort(iterable, descending=False):  # O(n + n log n)
    sign = -1 if descending else 1

    h = iterable[:]  # O(n)
    h = [sign * el for el in h]  # O(n)
    heapq.heapify(h)
    return [sign * heapq.heappop(h) for _ in range(len(h))]  # O(n log n)


nums = [23, 54, 1, 2, 34, 12, 12, 22, 132, 90, 42, -13]
sorted_nums = heap_sort_simple(nums)
print(nums)
print(sorted_nums)

sorted_min = heap_sort(nums)
sorted_max = heap_sort(nums, True)

print(sorted_min)
print(sorted_max)
