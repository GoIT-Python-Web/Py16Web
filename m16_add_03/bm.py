def build_shift_table(pattern):
    """Створити таблицю зсувів для алгоритму Боєра-Мура."""
    table = {}
    length = len(pattern)
    # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = len(pattern) - 1
    while i < len(text):
        j = len(pattern) - 1
        # Порівняння символів тексту та підрядка
        while j >= 0 and text[i] == pattern[j]:
            i -= 1
            j -= 1
        # Якщо всі символи підрядка збігаються, повертаємо індекс у головному тексті
        if j < 0:
            return i + 1  # Початок підрядка
        # Інакше зсуваємо індекс у головному тексті на відповідне значення з таблиці зсувів
        i += shift_table.get(text[i], len(pattern))
    return -1


text = "Being a developer is not easy"
pattern = "developer"

shift_table = build_shift_table(pattern)
print(shift_table)

position = boyer_moore_search(text, pattern)
if position != -1:
    print(f"Substring found at index {position}")
else:
    print("Substring not found")
