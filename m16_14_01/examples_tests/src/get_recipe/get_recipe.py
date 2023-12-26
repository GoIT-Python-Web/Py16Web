def get_recipe(path, search_id):
    result = None  #
    with open(path, "r") as f:  #
        for line in f:  #
            (id, name, *recipes) = line.strip().split(",")  #
            if id == search_id:  #
                result = {"id": id, "name": name, "ingredients": recipes}  #
    return result  #


if __name__ == '__main__':
    result = get_recipe('ingredients.csv', "60b90c1c13067a15887e1ae1")
    print(result)
