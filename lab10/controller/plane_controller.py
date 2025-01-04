from domain.plane import Plane
from repository.plane_repository import PlaneRepository
from utils.utils import quick_sort, filter, form_k_groups
from collections import defaultdict


class PlaneController:

    def __init__(self, plane_repo: PlaneRepository):
        """
        Initialize the controller with a plane repository.

        Args:
            plane_repo (PlaneRepository): The repository managing Plane instances.

        Returns:
            None

        Raises:
            None
        """
        self.__repo = plane_repo

    def sort_by_pass_number(self):
        """
        Sort planes by the number of passengers in descending order.

        Returns:
            list[Plane]: A list of planes sorted by passenger count.

        Raises:
            None
        """
        planes = self.__repo.get_all_planes()
        return quick_sort(
            planes,
            key=lambda x: len(x.get_passager_list()),
            comp=lambda x, y: x > y,
        )

    def sort_by_passenger_number_first_name(self, substring: str):
        """
        Sort planes by the number of passengers whose first names start with a given substring.

        Args:
            substring (str): The substring to match at the start of passengers' first names.

        Returns:
            list[Plane]: A list of planes sorted based on the count of matching passengers.

        Raises:
            None
        """
        planes = self.__repo.get_all_planes()
        return quick_sort(
            planes,
            key=lambda plane: len([p for p in plane.get_passager_list() 
                                 if p.get_first_name().startswith(substring)]),
            comp=lambda x, y: x > y,
        )

    def sort_by_passenget_number_destination(self):
        """
        Sort planes first by passenger number (ascending) and then by destination.

        Returns:
            list[Plane]: A list of planes sorted by passenger number and destination.

        Raises:
            None
        """
        planes = self.__repo.get_all_planes()
        return quick_sort(
            planes,
            key=lambda plane: f"{len(plane.get_passager_list())}{plane.get_destination()}",
            comp=lambda x, y: x < y,
        )

    def filter_by_passenger_name(self, name: str):
        """
        Filter planes that have at least one passenger with the given first name.

        Args:
            name (str): The first name to filter passengers by.

        Returns:
            list[Plane]: A list of planes with at least one passenger matching the name.

        Raises:
            None
        """
        planes = self.__repo.get_all_planes()
        return filter(
            planes,
            lambda x: name
            in [passenger.get_first_name() for passenger in x.get_passager_list()],
        )

    def groups_different_last_name(self, k: int):
        """
        Form groups of k passengers from the same plane with different last names.

        Args:
            k (int): The size of the groups to form.

        Returns:
            dict: A dictionary with plane IDs as keys and lists of passenger groups as values.

        Raises:
            None
        """
        planes = self.__repo.get_all_planes()
        result = {}
        for plane in planes:
            passengers = plane.get_passager_list()
            # Get unique last names first
            unique_passengers = []
            seen_last_names = set()
            for p in passengers:
                if p.get_last_name() not in seen_last_names:
                    unique_passengers.append(p)
                    seen_last_names.add(p.get_last_name())
            
            if len(unique_passengers) >= k:
                groups = form_k_groups(k, unique_passengers)
                if groups:
                    result[plane.get_id()] = groups
        return result

    def goupt_by_destination(self, k: int):
        """
        Group planes by destination and form groups of size k.

        Args:
            k (int): The group size for planes at each destination.

        Returns:
            defaultdict: A dictionary with destinations as keys and lists of plane groups as values.

        Raises:
            None
        """
        planes = self.__repo.get_all_planes()

        destinations = set()
        for plane in planes:
            destinations.add(plane.get_destination())
        result = defaultdict(list)
        for destination in destinations:
            filtered_planes = filter(
                planes, key=lambda plane: plane.get_destination() == destination
            )

            if k >= len(filtered_planes):
                k_goups = form_k_groups(k, filtered_planes)
            result[destination].append(k_goups)
        
        return result

    def create_plane(self, plane: Plane):
        """
        Create a new plane and add it to the repository.

        Args:
            plane (Plane): The plane to add.

        Returns:
            None

        Raises:
            ValueError: If a plane with the same ID already exists.
        """
        self.__repo.create_plane(plane.get_id(), plane.get_company_name(), plane.get_seat_number(), plane.get_destination(), plane.get_passager_list())

    def update_plane(self, plane_id: str | int, company_name: str | None = None, seat_number: int | None = None,
                     destination: str | None = None, passengers_list: list | None = None):
        """
        Update an existing plane's details.

        Args:
            plane_id (str | int): The ID of the plane to update.
            company_name (str, optional): The new company name.
            seat_number (int, optional): The new seat number.
            destination (str, optional): The new destination.
            passengers_list (list, optional): The new list of passengers.

        Returns:
            None

        Raises:
            ValueError: If no plane with the given ID is found.
        """
        self.__repo.update_plane(plane_id, company_name, seat_number, destination, passengers_list)

    def get_all_planes(self) -> list[Plane]:
        """
        Retrieve all planes in the repository.

        Returns:
            list[Plane]: A list of all planes.

        Raises:
            None
        """
        return self.__repo.get_all_planes()

    def get_plane(self, plane_id: str | int) -> Plane:
        """
        Retrieve a plane by its ID.

        Args:
            plane_id (str | int): The ID of the plane to retrieve.

        Returns:
            Plane: The plane with the specified ID.

        Raises:
            ValueError: If no plane is found with the specified ID.
        """
        return self.__repo.get_plane(plane_id)

    def delete_plane(self, plane_id: str | int):
        """
        Delete a plane by its ID.

        Args:
            plane_id (str | int): The ID of the plane to delete.

        Returns:
            None

        Raises:
            ValueError: If no plane is found with the specified ID.
        """
        self.__repo.delete_plane(plane_id)
