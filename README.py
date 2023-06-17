def read_recipes(file_name):
    cook_book = {}
    with open(file_name, "r") as file:
        while True:
            recipe_name = file.readline().strip()
            if not recipe_name:
                break

            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_info = file.readline().strip().split(" | ")
                ingredient = {
                    "ingredient_name": ingredient_info[0],
                    "quantity": int(ingredient_info[1]),
                    "measure": ingredient_info[2],
                }
                ingredients.append(ingredient)

            cook_book[recipe_name] = ingredients

            file.readline()

    return cook_book


file_name = "recipes.txt"
cook_book = read_recipes(file_name)
print(cook_book)
