from recipe_repository import RecipeRepository
import sys


def print_menu():

    menu = [
        "1.Add a new recipie.",
        "2.Update a recipies preparation time by id.",
        "3.Delete all recipes bellow 10 min.",
        "4.Sort the recipes by name.",
        "5.Sort the recipes by difficulty descending.",
        "6.Print current recipes.",
        "0.Exit program.",
    ]

    for item in menu:
        print(item)


if __name__ == "__main__":

    print_menu()
    repo = RecipeRepository()
    repo.add_recipe(1, "Spaghetti Bolognese", "Italian", 3, 30)
    repo.add_recipe(2, "Miso Soup", "Mexican", 2, 15)
    repo.add_recipe(3, "Chicken Curry", "Indian", 4, 45)
    repo.add_recipe(4, "Fish and Chips", "Mexican", 2, 25)
    repo.add_recipe(5, "Tacos", "Mexican", 3, 20)
    repo.add_recipe(6, "French Toast", "Indian", 1, 10)
    repo.add_recipe(7, "Paella", "Indian", 4, 60)
    repo.add_recipe(8, "Sushi", "Indian", 5, 50)
    repo.add_recipe(9, "Hamburger", "Italian", 2, 15)
    repo.add_recipe(10, "Greek Salad", "Mexican", 1, 10)
    repo.add_recipe(11, "Greek Salad2", "Mexican", 1, 4)
    while True:
        try:
            op = int(input("Input the operation number: "))
        except ValueError:
            print("The input must be a int.")

        match op:
            case 0:
                sys.exit(0)
            case 1:
                try:
                    id = int(input("Input the recipe id: "))
                except ValueError:
                    print("The id must be of type int.")
                name = input("Input the name of the recipe: ")
                cuisine = input("Input the cuisine of the recipe: ")
                try:
                    difficulty = int(input("Input the difficulty of the recipe: "))
                except ValueError:
                    print("The difficulty must be of type int.")
                try:
                    preparation_time = int(
                        input("Input the preparation time of the recipe: ")
                    )
                except:
                    print("The preparation_time must be of type int.")
                try:
                    repo.add_recipe(id, name, cuisine, difficulty, preparation_time)
                except (ValueError, TypeError) as e:
                    print(e)
            case 2:
                try:
                    id = int(input("Input the recipe id: "))
                except ValueError:
                    print("The id must be of type int.")
                try:
                    preparation_time = int(
                        input("Input the preparation time of the recipe: ")
                    )
                except:
                    print("The preparation_time must be of type int.")
                try:
                    repo.update_by_id(id, preparation_time)
                except ValueError as e:
                    print(e)

            case 3:
                repo.delete_all_under_10_min()
                for recipe in repo.get_all():
                    print(recipe)
            case 4:
                for recipe in repo.sort_by_name():
                    print(recipe)
            case 5:
                for recipe in repo.sort_by_difficulty():
                    print(recipe)
            case 6:
                for recipe in repo.get_all():
                    print(recipe)
            case _:
                print("Not a valid operation")
