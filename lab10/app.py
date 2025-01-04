from domain.passager import Passager
from domain.plane import Plane
from repository.passager_repository import PassagerRepository
from repository.plane_repository import PlaneRepository
from controller.passager_controller import PassagerController
from controller.plane_controller import PlaneController
import os,sys
import random

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def airport_menu():
    menu_list = ["1. Create a new pane.",
                 "2. Display all the planes.",
                 "3. Update a plane.",
                 "4. Delete a plane.",
                 "5. Sort planes by passager number.",
                 "6. Sort planes by passagers first name",
                 "7. Sort planes by passagers first name and destination.",
                 "8. Filter planes by passagers first name.",
                 "9. Group planes by last name.",
                 "10. Group planes by destination.",
                 "0. Exit program."]

    for option in menu_list:
        print(option)


def generate_random_planes(n):
    destinations = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
    plane_types = ["Boeing 737", "Airbus A320", "Boeing 777", "Airbus A380", "Boeing 787"]
    first_names = ["John", "Jane", "Jake", "Jack", "Jill"]
    last_names = ["Doe", "Smith", "Brown", "Wilson", "Taylor"]
    planes = []
    for _ in range(n):
        plane_id = random.randint(1000, 9999)
        plane_type = random.choice(plane_types)
        destination = random.choice(destinations)
        seat_number = random.randint(1, 10)
        passengers = [
            Passager(random.choice(first_names), random.choice(last_names), random.randint(100, 999))
            for _ in range(random.randint(1, seat_number))
        ]
        plane = Plane(plane_id, plane_type, seat_number, destination, passengers)
        planes.append(plane)
    return planes


if __name__ == "__main__":

    plane_repo = PlaneRepository()
    aeroport = PlaneController(plane_repo)

    random_planes = generate_random_planes(10)
    for plane in random_planes:
        aeroport.create_plane(plane)
    clear_screen()  
    while True:
        airport_menu()
        try:
            op = int(input("Input the operation you want to preform: "))
        except ValueError:
            print("The operation must be a int.")
            clear_screen()
        
        match op:

            case 0:
                clear_screen()
                sys.exit(0)
            case 1:
                try:
                    plane_id = input("Enter plane ID: ")
                    company_name = input("Enter company name: ")
                    seat_number = int(input("Enter number of seats: "))
                    destination = input("Enter destination: ")
                    num_passengers = int(input("Enter number of passengers: "))
                    passengers = []
                    for _ in range(num_passengers):
                        first_name = input("Enter passenger's first name: ")
                        last_name = input("Enter passenger's last name: ")
                        passport_number = int(input("Enter passenger's passport number: "))
                        passenger = Passager(first_name, last_name, passport_number)
                        passengers.append(passenger)
                    plane = Plane(plane_id, company_name, seat_number, destination, passengers)
                    aeroport.create_plane(plane)
                    print("Plane created successfully.")
                except ValueError as ve:
                    print(f"Invalid input: {ve}")
                except Exception as e:
                    print(f"Error: {e}")
            case 2:
                for plane in aeroport.get_all_planes():
                    print(plane,end="\n\n")
            case 3:
                try:
                    plane_id = input("Enter the ID of the plane to update: ")
                    company_name = input("Enter new company name (leave blank to keep current): ")
                    seat_number_input = input("Enter new number of seats (leave blank to keep current): ")
                    destination = input("Enter new destination (leave blank to keep current): ")
                    
                    updates = {}
                    if company_name:
                        updates['company_name'] = company_name
                    if seat_number_input:
                        updates['seat_number'] = int(seat_number_input)
                    if destination:
                        updates['destination'] = destination
                    
                    if updates:
                        aeroport.update_plane(plane_id, **updates)
                        print("Plane updated successfully.")
                    else:
                        print("No updates provided.")
                except ValueError as ve:
                    print(f"Invalid input: {ve}")
                except Exception as e:
                    print(f"Error: {e}")
            case _:
                print("Input a valid operation.")





