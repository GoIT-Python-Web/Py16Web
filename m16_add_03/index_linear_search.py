# Основний відсортований масив
main_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]


def create_index_table(array, step):
    index_table = []
    for i in range(0, len(array), step):
        index_table.append((array[i], i))
    return index_table


# Створення індексної таблиці з кроком 4
index_table = create_index_table(main_array, 4)
print(index_table)


# Функція для індексно-послідовного пошуку
def indexed_sequential_search(array, index_table, target):
    # Пошук в індексній таблиці
    start = 0
    end = len(index_table) - 1
    while start <= end:
        mid = (start + end) // 2
        if index_table[mid][0] == target:
            return index_table[mid][1]
        elif index_table[mid][0] < target:
            start = mid + 1
        else:
            end = mid - 1

    # Визначення діапазону для послідовного пошуку
    if start == 0:
        search_range = (0, index_table[0][1])
    elif start >= len(index_table):
        search_range = (index_table[-1][1], len(array))
    else:
        search_range = (index_table[start - 1][1], index_table[start][1])

    # Послідовний пошук в діапазоні
    for i in range(search_range[0], search_range[1]):
        if array[i] == target:
            return i
    return -1  # якщо елемент не знайдено


target = 15
result = indexed_sequential_search(main_array, index_table, target)
if result != -1:
    print(f"Елемент {target} знайдено на позиції {result}")
else:
    print(f"Елемент {target} не знайдено")