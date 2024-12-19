from domain.passager import Passager

class PassagerRepository:

    def __init__(self, passager_list: list[Passager] | None = None):
        """
        Initialize the repository with an optional list of passengers.

        Args:
            passager_list (list[Passager], optional): A list of Passager objects to initialize the repository.

        Returns:
            None

        Raises:
            None
        """
        self.__passagers = passager_list if passager_list is not None else []

    def create_passager(self, passager: Passager):
        """
        Add a new passenger to the repository.

        Args:
            passager (Passager): The passenger to add.

        Returns:
            None

        Raises:
            ValueError: If a passenger with the same passport number already exists.
        """
        for existing in self.__passagers:
            if existing.get_passport_number() == passager.get_passport_number():
                raise ValueError(f"Passager with passport number {passager.get_passport_number()} already exists.")
        self.__passagers.append(passager)

    def update_passager(
        self,
        check_first_name: str | None = None,
        passport_number: int | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
    ):
        """
        Update an existing passenger's information.

        Args:
            check_first_name (str, optional): The first name to match for updating.
            passport_number (int, optional): The passport number to match for updating.
            first_name (str, optional): The new first name.
            last_name (str, optional): The new last name.

        Returns:
            None

        Raises:
            ValueError: If neither 'check_first_name' nor 'passport_number' is provided or no matching passenger is found.
        """
        if check_first_name is None and passport_number is None:
            raise ValueError("You must specify either 'check_first_name' or 'passport_number' to find the Passager.")

        for passager in self.__passagers:
            if (
                (check_first_name and passager.get_first_name() == check_first_name) or
                (passport_number and passager.get_passport_number() == passport_number)
            ):
                if first_name is not None:
                    passager.set_first_name(first_name)
                if last_name is not None:
                    passager.set_last_name(last_name)
                if passport_number is not None:
                    passager.set_passport_number(passport_number)
                return
        raise ValueError("No matching Passager found.")

    def get_all(self) -> list[Passager]:
        """
        Retrieve all passengers in the repository.

        Args:
            None

        Returns:
            list[Passager]: A list of all passengers.

        Raises:
            None
        """
        return self.__passagers[:]

    def get_passager(self, passport_number: int) -> Passager:
        """
        Retrieve a passenger by passport number.

        Args:
            passport_number (int): The passport number of the passenger to retrieve.

        Returns:
            Passager: The passenger with the specified passport number.

        Raises:
            ValueError: If no passenger is found with the specified passport number.
        """
        for passager in self.__passagers:
            if passager.get_passport_number() == passport_number:
                return passager
        raise ValueError(f"No Passager found with passport number {passport_number}")

    def delete(self, passport_number: int):
        """
        Delete a passenger by passport number.

        Args:
            passport_number (int): The passport number of the passenger to delete.

        Returns:
            None

        Raises:
            ValueError: If no passenger is found with the specified passport number.
        """
        for i, passager in enumerate(self.__passagers):
            if passager.get_passport_number() == passport_number:
                self.__passagers.pop(i)
                return
        raise ValueError(f"No Passager found with passport number {passport_number}")
