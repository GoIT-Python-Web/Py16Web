Напомним, что в 4 модуле мы для кулинарного блога писали функцию `format_ingredients`, которая принимала на вход список
из ингредиентов рецепта.

Мы продолжим работать в этом направлении и создадим функцию, которая будет искать рецепт в файле и возвращать найденный
рецепт в виде словаря определенной формы.

У вас есть файл, который содержит рецепты в виде:

```
60b90c1c13067a15887e1ae1,Herbed Baked Salmon,4 lemons,1 large red onion,2 tablespoons chopped fresh basil
60b90c2413067a15887e1ae2,Lemon Pancakes,2 tablespoons baking powder,1 cup vanilla-flavored almond milk,1 lemon
60b90c2e13067a15887e1ae3,Chicken and Cold Noodles,6 ounces dry Chinese noodles,1 tablespoon sesame oil,3 tablespoons soy sauce
60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese
60b90c4613067a15887e1ae5,State Fair Lemonade,6 lemons,1 cups white sugar,5 cups cold water
```

Каждый рецепт записан с новой строки (не забываем при решении задачи про конец строки). Каждая запись начинается с
первичного ключа базы данных MongoDB. Дальше, через запятую, идет название рецепта, а после, через запятую, идет
перечисление ингредиентов рецепта.

Вам необходимо реализовать функцию, чтобы получать информацию о рецепте в виде словаря для каждого искомого блюда.
Создайте функцию `get_recipe(path, search_id)`, которая будет возвращать словарь для рецепта с указанным идентификатором
MongoDB.

Где параметры функции:

- `path` &mdash; путь к файлу.
- `search_id` &mdash; первичный ключ MongoDB для поиска рецепта.

Требования:

- Используйте менеджер контекста `with` для чтения из файла
- Если рецепта с указанным `search_id` в файле нет, функция должна вернуть `None`

Пример: для файла, указанного выше, вызов функции в виде

```python
get_recipe("./data/ingredients.csv", "60b90c3b13067a15887e1ae4")
```

Должен найти в файле
строку `60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese`
и вернуть результат в виде словаря такой структуры:

```python
{
    "id": "60b90c3b13067a15887e1ae4",
    "name": "Watermelon Cucumber Salad",
    "ingredients": [
        "1 large seedless watermelon",
        "12 leaves fresh mint",
        "1 cup crumbled feta cheese",
    ],
}
```
