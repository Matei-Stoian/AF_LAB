import random
from F1 import feature01
from F2 import feature02
from F3 import feature03
from F4 import feature04
from F5 import feature05
import os

list_stack = []
original_list = []


def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def undo() -> list[int]:
    """
    Returns the last version of the list before the most recent modification.
    """
    global list_stack
    global original_list
    if list_stack:
        return list_stack.pop()
    else:
        return original_list


def print_menu():
    clear_console()
    print("1. Add a value to the end of the list.")
    print("2. Insert a value at a specific position.")
    print("3. Remove a value from a specific position.")
    print("4. Remove values within a specific interval.")
    print("5. Replace a value at a specific position.")
    print("6. Return all elements smaller than a given value.")
    print("7. Return the sorted list.")
    print("8. Return all elements greater than a given value.")
    print("9. Compute the average of elements in the list.")
    print("10. Return the minimum value in the list.")
    print("11. Multiply all values in the list by a given value.")
    print("12. Filter out values smaller than or equal to a given value.")
    print("13. Filter out values that are not multiples of a given value.")
    print("14. Undo the last operation.")
    print("15. Print the current list.")
    print("0. Exit the program.")
    print("-1. Show the menu again.")


def options_menu():
    """
    Displays an interactive menu for performing various list operations, including
    adding, removing, replacing, filtering, sorting, and undoing changes to a list.
    """
    global list_stack
    global original_list
    #score_list = [random.randint(0, 101) for _ in range(10)]
    score_list = read_list_file()
    original_list = score_list.copy()
    print_menu()

    try:
        with open("output.txt", "w") as w:
            while True:
                try:
                    op = int(input("Select an operation to perform on the list: "))
                except ValueError:
                    print("The operation must be an integer.\n")
                    continue

                match op:
                    case -1:
                        print_menu()
                    case 0:
                        exit(0)
                    case 1:
                        try:
                            val = int(input("Enter the value to append to the list: "))
                            list_stack.append(score_list.copy())
                            score_list = feature01.add(score_list, val)
                            w.write(",".join(map(str, score_list)) + "\n")
                            print(score_list)
                        except ValueError:
                            print("The value must be an integer.\n")
                    case 2:
                        try:
                            val = int(
                                input("Enter the value to insert into the list: ")
                            )
                            idx = int(
                                input(
                                    "Enter the index where the value should be inserted: "
                                )
                            )
                            list_stack.append(score_list.copy())
                            score_list = feature01.insert(score_list, idx, val)
                            print(score_list)
                            w.write(",".join(map(str, score_list)) + "\n")
                        except ValueError:
                            print("Both value and index must be integers.\n")
                    case 3:
                        try:
                            idx = int(
                                input(
                                    "Enter the index of the value to remove from the list: "
                                )
                            )
                            list_stack.append(score_list.copy())
                            score_list = feature02.remove(score_list, idx)
                            print(score_list)
                            w.write(",".join(map(str, score_list)) + "\n")
                        except ValueError:
                            print("The index must be an integer.\n")
                    case 4:
                        try:
                            idx_start = int(
                                input(
                                    "Enter the starting index of the range to remove: "
                                )
                            )
                            idx_end = int(
                                input("Enter the ending index of the range to remove: ")
                            )
                            list_stack.append(score_list.copy())
                            score_list = feature02.remove(
                                score_list, idx_start, idx_end
                            )
                            print(score_list)
                            w.write(",".join(map(str, score_list)) + "\n")
                        except ValueError:
                            print("Both indices must be integers.\n")
                    case 5:
                        try:
                            val = int(input("Enter the value to replace: "))
                            idx = int(
                                input(
                                    "Enter the index where the value should be replaced: "
                                )
                            )
                            list_stack.append(score_list.copy())
                            score_list = feature02.replace(score_list, idx, val)
                            print(score_list)
                            w.write(",".join(map(str, score_list)) + "\n")
                        except ValueError:
                            print("Both value and index must be integers.\n")
                    case 6:
                        try:
                            val = int(input("Enter the value to compare with: "))
                            print(feature03.less(score_list, val))
                            w.write(",".join(map(str, feature03.less(score_list, val))))
                        except ValueError:
                            print("The value must be an integer.\n")
                    case 7:
                        w.write(
                            ",".join(map(str, feature03.sort_score(score_list))) + "\n"
                        )
                        print(feature03.sort_score(score_list))
                    case 8:
                        try:
                            val = int(input("Enter the value to compare with: "))
                            print(feature03.higher(score_list, val))
                            w.write(
                                ",".join(map(str, feature03.higher(score_list, val)))
                                + "\n"
                            )
                        except ValueError:
                            print("The value must be an integer.\n")
                    case 9:
                        try:
                            idx_start = int(
                                input("Enter the starting index for averaging: ")
                            )
                            idx_end = int(
                                input("Enter the ending index for averaging: ")
                            )
                            print(feature04.avg(score_list, idx_start, idx_end))
                            
                        except ValueError:
                            print("Both indices must be integers.\n")
                    case 10:
                        try:
                            idx_start = int(
                                input("Enter the starting index for finding minimum: ")
                            )
                            idx_end = int(
                                input("Enter the ending index for finding minimum: ")
                            )
                            print(feature04.find_min(score_list, idx_start, idx_end))
                            w.write(
                                ",".join(
                                    map(
                                        str,
                                        feature04.find_min(
                                            score_list, idx_start, idx_end
                                        ),
                                    )
                                )
                                + "\n"
                            )
                        except ValueError:
                            print("Both indices must be integers.\n")
                    case 11:
                        try:
                            idx_start = int(
                                input("Enter the starting index for multiplication: ")
                            )
                            idx_end = int(
                                input("Enter the ending index for multiplication: ")
                            )
                            multiplier = int(input("Enter the value to multiply by: "))
                            print(
                                feature04.mul(
                                    score_list, multiplier, idx_start, idx_end
                                )
                            )
                            w.write(
                                ",".join(
                                    map(
                                        str,
                                        feature04.mul(
                                            score_list, multiplier, idx_start, idx_end
                                        ),
                                    )
                                )
                                + "\n"
                            )
                        except ValueError:
                            print("The values must be integers.\n")
                    case 12:
                        try:
                            val = int(input("Enter the value to compare with: "))
                            list_stack.append(score_list.copy())
                            score_list = feature05.filter_greater(score_list, val)
                            print(score_list)
                            w.write(",".join(map(str, score_list)) + "\n")
                        except ValueError:
                            print("The value must be an integer.\n")
                    case 13:
                        try:
                            val = int(input("Enter the value to check for multiples: "))
                            list_stack.append(score_list.copy())
                            score_list = feature05.filter_mul(score_list, val)
                            print(score_list)
                            w.write(",".join(map(str, score_list)) + "\n")
                        except ValueError:
                            print("The value must be an integer.\n")
                    case 14:
                        score_list = undo()
                        w.write(",".join(map(str, score_list)) + "\n")
                        print(score_list)
                    case 15:
                        print(score_list)
                        w.write(",".join(map(str, score_list)) + "\n")
                    case _:
                        print("Please enter a valid operation number (0-15).\n")

    except IOError as e:
        print("Error openeing the file: ", e)


def read_list_file() -> list[int]:
    try:
        with open("input.txt", "r") as f:
            try:
                score_list = list(map(int, f.read().split(",")))
                return score_list
            except ValueError:
                print("All values from the score list must be integers.")
    except IOError as e:
        print(f"Error oppening the file: {e}")


if __name__ == "__main__":
    options_menu()
