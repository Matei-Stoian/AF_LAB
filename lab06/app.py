import os
from pointrepository import PointRepository
from mypoint import MyPoint
import random


def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def print_menu():
    clear_console()
    print("1. Add a point to the repository.")
    print("2. Get all the points from the repository.")
    print("3. Get points of a specific color.")
    print("4. Calculate the minimum distance between points.")
    print("5. Get points inside the square.")
    print("6. Remove points from the square.")
    print("7. Update a point at a specific index.")
    print("8. Remove point from a specific index.")
    print("9. Plot all the points")
    print("10. Calculate the maximum distance between points.")
    print("11. Shift all points to have x=0.")
    print("12. Delete points inside a circle.")
    print("0. Exit program.")
    print("-1. Print the menu.")


def print_points(points):

    for point in points:
        print(str(point))


def handle_input():
    repository = PointRepository()

    for _ in range(10):
        x = random.uniform(-3, 3)
        y = random.uniform(-3, 3)
        color = random.choice(["red", "green", "blue", "yellow", "magenta"])
        repository.addPoint(MyPoint(x, y, color))

    print_menu()
    while True:
        try:
            op = int(input("Select an operation to preform: "))
        except ValueError:
            print("The operation must be an integer.\n")
            continue

        match op:
            case 0:
                exit(0)
            case 1:
                try:
                    x = float(input("Enter x coordinate: "))
                    y = float(input("Enter y coordinate: "))
                    color = input("Enter color: ")
                    try:
                        new_point = MyPoint(x, y, color)
                        repository.addPoint(new_point)
                    except Exception as e:
                        print(e)
                except ValueError:
                    print("Input only float for the coordinates.\n")
            
            case 2:
                points = repository.getAllPoints()
                print_points(points)
            case 3:
                color = input("Enter color: ")
                if color not in ["red", "green", "blue", "yellow", "magenta"]:
                    print("Not a valid color.\n")
                    continue
                points = repository.getAllPointsColor(color)
                print_points(points)
            case 4:
                print(f"Minumum distance = {repository.minDistance()}")
            case 5:
                try:
                    x = float(input("Enter x coordinates for the top-left corner: "))
                    y = float(input("Enter y coordinates for the top-left corner: "))
                    lenght = int(input("Enter the lenght of the side of the square: "))
                    points = repository.getPointsInSquare((x,y),lenght)
                    print_points(points)
                except ValueError:
                    print("The coordinates must be float and the lenght int.\n")
            case 6:
                try:
                    x = float(input("Enter x coordinates for the top-left corner: "))
                    y = float(input("Enter y coordinates for the top-left corner: "))
                    lenght = int(input("Enter the lenght of the side of the square: "))
                    nums = repository.removePointsFromSquare((x,y),lenght)
                    print(f"Deleted points = {nums}")
                except ValueError:
                    print("The coordinates must be float and the lenght int.\n")
            case 7:
                try:
                    idx = int(input("Enter the index: "))
                    x = float(input("Enter x coordinate: "))
                    y = float(input("Enter y coordinate: "))
                    color = input("Enter color: ")
                    try:
                        new_point = MyPoint(x,y,color)
                        repository.updatePoint(idx,new_point)
                    except Exception as e:
                        print(e)
                except ValueError:
                    print("The index must be int and the coordinates must be float.\n")
               
            case 8:
                try:
                    idx = int(input("Enter the index: "))
                    try:
                        repository.removePoint(idx)
                    except IndexError:
                        print("Index of range.\n")
                except ValueError:
                    print("The index must be int.\n")
    
            case 9:
                repository.plot()
            case 10:
                print(f"Max distance is {repository.getMaxDist()}")
            case 11:
                repository.shiftPointsY()
                print("Points had been shifted.")
            case 12:
                try:
                    x = float(input("Enter x coordinate: "))
                    y = float(input("Enter y coordinate: "))
                    radius = int(input("Enter the circle radius: "))
                    nums = repository.deleteAllInsideCircle(MyPoint(x,y,None),radius)
                    print(f"Deleted points = {nums}")
                except ValueError:
                    print("The radius must be an int and the rest float\n.")
            case -1:
                print_menu()
            case _:
                print("Invalid option. Please try again.")





if __name__ == "__main__":
    handle_input()
