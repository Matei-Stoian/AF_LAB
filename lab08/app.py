import os
from vectorrepository import VectorRepository
from myvector import MyVector
import random


def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def print_menu():
    clear_console()
    print("1. Add a vector to the repository.")
    print("2. Get all the vectors from the repository.")
    print("3. Get vector from the repository by index.")
    print("4. Update vector by index.")
    print("5. Update vector by name_id.")
    print("6. Delete a vector by index.")
    print("7. Delete a vector by name_id.")
    print("8. Plot the vectors.")
    print("9. Get the sum of all vectors.")
    print("10. Delete all the vecotrs from the repository.")
    print(
        "11. Set the color of a vector to specific color for all the vectors with a specific type_id."
    )
    print("0. Exit program.")
    print("-1. Print the menu.")


def print_vector(vector: MyVector):
    print(str(vector))


def handle_input():
    print_menu()
    repo = VectorRepository()

    colors = ["r", "y", "g", "b", "m"]
    for _ in range(10):
        name_id = random.choice(
            [random.randint(1, 100), f"name_{random.randint(1, 100)}"]
        )
        color = random.choice(colors)
        vector_type = random.randint(1, 8)
        values = [random.randint(-50, 50) for _ in range(3)]

        vector = MyVector(name_id=name_id, color=color, type=vector_type, values=values)
        repo.add_vector(vector)

    while True:
        try:
            option = int(input("Choose one operation to preforme: "))
        except TypeError:
            print("The options must be a int.")

        match option:

            case -1:
                print_menu()
            case 0:
                exit(0)
            case 1:
                name_id = input("Name_id: ")
                if name_id.isdigit():
                    name_id = int(name_id)
                color = input("Color: ")
                type = int(input("Type: "))
                try:
                    values = list(map(int, input("Vector values: ").split(" ")))
                except ValueError:
                    pass
                try:
                    vector = MyVector(
                        name_id=name_id, color=color, type=type, values=values
                    )
                    repo.add_vector(vector=vector)
                except ValueError as e:
                    print(e)
            case 2:
                vectors = repo.get_all_vectors()
                for vector in vectors:
                    print_vector(vector)

            case 3:
                try:
                    index = int(input("Index: "))
                except ValueError:
                    print("The index must be int.")
                try:
                    vector = repo.get_vector_by_index(index)
                    print_vector(vector)
                except IndexError as e:
                    print(e)
            case 4:
                try:
                    index = int(input("Index: "))
                except ValueError:
                    print("The index must be int.")
                    continue

                name_id = input("Name_id: ")
                if name_id == "":
                    name_id = None
                elif name_id.isdigit():
                    name_id = int(name_id)
                color = input("Color: ")
                if color == "":
                    color = None
                type = input("Type: ")
                if type == "":
                    type = None
                else:
                    try:
                        type = int(type)
                    except ValueError:
                        print("Type must be of type int.")
                try:
                    ipt = input("Vector values: ")
                    if ipt == "":
                        values = None
                    else:
                        values = list(map(int, ipt.split(" ")))
                except ValueError:
                    print("All the values must be a of type int.")

                try:
                    repo.update_vector_by_index(index,name_id,color,vector_type=type,values=values)
                except IndexError as e:
                    print(e)
            case 5:
                check_name_id = input("Check Name_id: ")
                if check_name_id.isdigit():
                    check_name_id = int(check_name_id)
                
                name_id = input("Name_id: ")
                if name_id == "":
                    name_id = None
                elif name_id.isdigit():
                    name_id = int(name_id)
                color = input("Color: ")
                if color == "":
                    color = None
                type = input("Type: ")
                if type == "":
                    type = None
                else:
                    try:
                        type = int(type)
                    except ValueError:
                        print("Type must be of type int.")
                try:
                    ipt = input("Vector values: ")
                    if ipt == "":
                        values = None
                    else:
                        values = list(map(int, ipt.split(" ")))
                except ValueError:
                    print("All the values must be a of type int.")

                try:
                    repo.update_vector_by_name_id(check_name_id,name_id=name_id,color=color,vector_type=type,values=values)
                except IndexError as e:
                    print(e)
            case 6:
                try:
                    index = int(input("Index"))
                except ValueError:
                    print("Index must be a int.")
                try:
                    repo.delete_vector_by_index(index)
                except IndexError as e:
                    print(e)
            case 7:
                check_name_id = input("Check Name_id: ")
                if check_name_id.isdigit():
                    check_name_id = int(check_name_id)
                try:
                    repo.delete_vector_by_name_id(check_name_id)
                except ValueError as e:
                    print(e)
            case 8:
                repo.plot__vectors()
            case 9:
                print(f"The sum is: {repo.get_sum_of_all__vectors()}")
            case 10:
                repo.delete_all__vectors()
            case 11:
                try:
                    type = int(input("Type: "))
                except ValueError:
                    print("The vector type must be a int.")
                color = input("Color: ")
                try:
                    repo.set_color_for_type(vector_type=type,color=color)
                except ValueError as e:
                    print(e)
            case _:
                print("Input a valid opperation.")


if __name__ == "__main__":
    handle_input()
