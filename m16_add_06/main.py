import heapq

numbers = [4, 10, 3, 5, 1]

# Min Heap
heapq.heapify(numbers)
print(numbers)

numbers = [4, 10, 3, 5, 1]

# Max Heap
temp_numbers = [el * -1 for el in numbers]
heapq.heapify(temp_numbers)
numbers = [el * -1 for el in temp_numbers]
print(numbers)
# ----------------------------------------------------------------

numbers = [4, 10, 3, 5, 1]

# Min Heap
heapq.heapify(numbers)
heapq.heappush(numbers, 23)
heapq.heappush(numbers, 2)
print(numbers)
min_element = heapq.heappop(numbers)
print(min_element)
print(numbers)

# додать елемент, а потім повернути
min_element = heapq.heappushpop(numbers, 13)
print(min_element)
print(numbers)

# повернути найменший елемент а потім додати елемент
min_element = heapq.heapreplace(numbers, 1)
print(min_element)
print(numbers)

# 2 найменший

two_min = heapq.nsmallest(2, numbers)
print(two_min, numbers)

two_max = heapq.nlargest(2, numbers)
print(two_max, numbers)


