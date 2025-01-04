from domain.plane import Plane


class PlaneRepository:
    def __init__(self, plane_list: list[Plane] | None = None):
        """
        Initialize the repository with an optional list of planes.

        Args:
            plane_list (list[Plane], optional): A list of Plane objects to initialize the repository.

        Returns:
            None

        Raises:
            None
        """
        self.__planes = plane_list if plane_list is not None else []

    def create_plane(
        self,
        plane_id: str | int,
        company_name: str,
        seat_number: int,
        destination: str,
        passengers_list: list,
    ):
        """
        Create a new plane and add it to the repository.

        Args:
            plane_id (str | int): The unique identifier for the plane.
            company_name (str): The name of the company operating the plane.
            seat_number (int): The number of seats available on the plane.
            destination (str): The destination of the plane.
            passengers_list (list): A list of passengers on the plane.

        Returns:
            None

        Raises:
            ValueError: If a plane with the given ID already exists.
        """
        for existing in self.__planes:
            if existing.get_id() == plane_id:
                raise ValueError(f"Plane with ID {plane_id} already exists.")
        new_plane = Plane(
            plane_id, company_name, seat_number, destination, passengers_list
        )
        self.__planes.append(new_plane)

    def update_plane(
        self,
        plane_id: str | int,
        company_name: str | None = None,
        seat_number: int | None = None,
        destination: str | None = None,
        passengers_list: list | None = None,
    ):
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
        for plane in self.__planes:
            if plane.get_id() == plane_id:
                if company_name is not None:
                    plane.set_company_name(company_name)
                if seat_number is not None:
                    plane.set_seat_number(seat_number)
                if destination is not None:
                    plane.set_destination(destination)
                if passengers_list is not None:
                    plane.set_passager_list(passengers_list)
                return
        raise ValueError(f"No plane found with ID {plane_id}.")

    def get_all_planes(self) -> list[Plane]:
        """
        Get a list of all planes in the repository.

        Returns:
            list[Plane]: A list of all planes.

        Raises:
            None
        """
        return self.__planes[:]

    def get_plane(self, plane_id: str | int) -> Plane:
        """
        Retrieve a plane by its ID.

        Args:
            plane_id (str | int): The ID of the plane to retrieve.

        Returns:
            Plane: The plane with the specified ID.

        Raises:
            ValueError: If no plane with the given ID is found.
        """
        for plane in self.__planes:
            if plane.get_id() == plane_id:
                return plane
        raise ValueError(f"No plane found with ID {plane_id}.")

    def delete_plane(self, plane_id: str | int):
        """
        Delete a plane from the repository by its ID.

        Args:
            plane_id (str | int): The ID of the plane to delete.

        Returns:
            None

        Raises:
            ValueError: If no plane with the given ID is found.
        """
        for i, plane in enumerate(self.__planes):
            if plane.get_id() == plane_id:
                self.__planes.pop(i)
                return
        raise ValueError(f"No plane found with ID {plane_id}.")
