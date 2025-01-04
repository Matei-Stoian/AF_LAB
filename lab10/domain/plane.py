from domain.passager import Passager
from repository.passager_repository import PassagerRepository

class Plane:

    def __init__(
        self,
        id: str | int,
        company_name: str,
        seat_number: int,
        destination: str,
        passengers_list: list[Passager],
    ):
        """
        Initialize a Plane with the given details.

        Args:
            id (str | int): The unique identifier of the plane.
            company_name (str): The name of the airline company.
            seat_number (int): The number of seats on the plane.
            destination (str): The destination of the plane.
            passengers_list (list[Passager]): The list of passengers on the plane.

        Returns:
            None

        Raises:
            TypeError: If any argument is of incorrect type.
            ValueError: If 'seat_number' is negative.
        """
        if not isinstance(id, str | int):
            raise TypeError("The id must be a int or a string.")
        self.__id = id
        if not isinstance(company_name, str):
            raise TypeError("The company name must be a string.")
        self.__company_name = company_name
        if not isinstance(seat_number, int):
            raise TypeError("The seat number must be a int.")
        if seat_number < 0:
            raise ValueError("The seat number must be positiv.")
        self.__seat_number = seat_number

        if not isinstance(destination, str):
            raise TypeError("The destination must be a string.")
        self.__destination = destination

        for passager in passengers_list:
            if not isinstance(passager, Passager):
                raise TypeError(
                    "All the objects from passager the list must by of type Passager."
                )
        self.__passagers_list = PassagerRepository(passengers_list)

    def get_id(self):
        """
        Get the plane's ID.

        Returns:
            str | int: The plane's unique identifier.
        """
        return self.__id

    def get_company_name(self):
        """
        Get the plane's company name.

        Returns:
            str: The name of the airline company.
        """
        return self.__company_name

    def get_seat_number(self):
        """
        Get the plane's seat number.

        Returns:
            int: The number of seats on the plane.
        """
        return self.__seat_number

    def get_destination(self):
        """
        Get the plane's destination.

        Returns:
            str: The destination of the plane.
        """
        return self.__destination

    def get_passager_list(self):
        """
        Get the list of passengers on the plane.

        Returns:
            list[Passager]: A copy of the passenger list.
        """
        return self.__passagers_list.get_all()

    def set_id(self, id):
        """
        Set the plane's ID.

        Args:
            id (str | int): The new ID for the plane.

        Returns:
            None

        Raises:
            TypeError: If 'id' is not a string or integer.
        """
        if not isinstance(id, str | int):
            raise TypeError("The id must be a int or a string.")
        self.__id = id

    def set_company_name(self, company_name):
        """
        Set the plane's company name.

        Args:
            company_name (str): The new company name.

        Returns:
            None

        Raises:
            TypeError: If 'company_name' is not a string.
        """
        if not isinstance(company_name, str):
            raise TypeError("The company name must be a string.")
        self.__company_name = company_name

    def set_seat_number(self, seat_number):
        """
        Set the plane's seat number.

        Args:
            seat_number (int): The new seat number.

        Returns:
            None

        Raises:
            TypeError: If 'seat_number' is not an integer.
            ValueError: If 'seat_number' is negative.
        """
        if not isinstance(seat_number, int):
            raise TypeError("The seat number must be a int.")
        if seat_number < 0:
            raise ValueError("The seat number must be positiv.")
        self.__seat_number = seat_number

    def set_destination(self, destination):
        """
        Set the plane's destination.

        Args:
            destination (str): The new destination.

        Returns:
            None

        Raises:
            TypeError: If 'destination' is not a string.
        """
        if not isinstance(destination, str):
            raise TypeError("The destination must be a string.")
        self.__destination = destination

    def set_passager_list(self, passager_list):
        """
        Set the list of passengers on the plane.

        Args:
            passager_list (list[Passager]): The new list of passengers.

        Returns:
            None

        Raises:
            TypeError: If any element in 'passager_list' is not a Passager instance.
        """
        for passager in passager_list:
            if not isinstance(passager, Passager):
                raise TypeError(
                    "All the objects from passager the list must by of type Passager."
                )
        self.__passagers_list = PassagerRepository(passager_list)

    def __repr__(self):
        return (f"Plane(id={self.__id}, company_name='{self.__company_name}', "
                f"seat_number={self.__seat_number}, destination='{self.__destination}', "
                f"passengers={self.__passagers_list.get_all()})")


