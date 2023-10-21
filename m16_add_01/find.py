import hashlib
import os

hashes = {}


def get_hash(path):
    """Повертає хеш-значення для файлу."""
    with open(path, 'rb') as file:
        bytes = file.read()
        readable_hash = hashlib.md5(bytes).hexdigest()
        return readable_hash


def find_duplicates(directory):
    """Шукає дублікати в директорії."""

    duplicates = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            file_hash = get_hash(path)
            if file_hash not in hashes:
                hashes[file_hash] = path
            else:
                duplicates.append((path, hashes[file_hash]))
    return duplicates


# Пошук дублікатів у заданій директорії
duplicates = find_duplicates('picture')
for duplicate in duplicates:
    print(f"Дублікатні файли: {duplicate[0]} та {duplicate[1]}")

print(hashes)
