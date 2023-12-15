from math import sqrt
from itertools import combinations


def held_karp(distance_matrix):  # O(n^2 * 2^n)
    n = len(distance_matrix)
    # Ініціалізація таблиці динамічного програмування
    # Та використання кортежів для представлення наборів міст
    dp = {(frozenset([0, i]), i): (distance_matrix[0][i], [0, i]) for i in range(1, n)}
    # Встановити базовий випадок - відстань від першого міста до себе дорівнює 0
    dp[(frozenset([0]), 0)] = (0, [0])

    # Перебираємо підмножини зростаючого розміру і знаходимо мінімальну відстань до кінцевого міста
    for r in range(2, n + 1):
        for subset in combinations(range(1, n), r):
            subset = frozenset(subset) | frozenset([0])
            for next_city in subset:
                if next_city == 0:
                    continue
                prev_subset = subset - frozenset([next_city])
                dp[(subset, next_city)] = min(
                    (
                        dp[(prev_subset, last_city)][0]
                        + distance_matrix[last_city][next_city],
                        dp[(prev_subset, last_city)][1] + [next_city],
                    )
                    for last_city in prev_subset
                    if last_city != 0
                )

    # Знаходимо мінімальну вартість, щоб завершити тур і повернутися до початкового міста
    all_cities = frozenset(range(n))
    result = min(
        (
            dp[(all_cities, last_city)][0] + distance_matrix[last_city][0],
            dp[(all_cities, last_city)][1] + [0],
        )
        for last_city in range(1, n)
    )
    print(dp)
    return result


# Функція для обчислення відстані між двома точками
def calculate_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


if __name__ == '__main__':

    # Словник із координатами міст
    cities = {"A": (0, 0), "B": (1, 5), "C": (2, 2), "D": (3, 3), "E": (5, 1)}

    # Створення матриці відстаней
    distance_matrix = []
    for i, source in enumerate(cities.values()):
        distance_matrix.append([])
        for target in cities.values():
            # Додавання розрахованої відстані до матриці
            distance_matrix[i].append(calculate_distance(source, target))

    # Виклик функції алгоритму з матрицею відстаней
    for i in range(len(distance_matrix[0])):
        print(distance_matrix[i])

    result, path = held_karp(distance_matrix)
    print(result, path)
    # Переводимо шлях від індексів до назв міст
    city_names = list(cities.keys())
    path_with_names = [city_names[i] for i in path]

    print(result, path_with_names)