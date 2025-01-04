class Passager:
    def __init__(self, first_name: str, last_name: str, passport_number: int):
        """
        Initialize a Passenger with the given details.

        Args:
            first_name (str): The first name of the passenger.
            last_name (str): The last name of the passenger.
            passport_number (int): The passport number of the passenger.

        Returns:
            None

        Raises:
            ValueError: If any argument is of incorrect type.
        """
        if not isinstance(first_name, str):
            raise ValueError("First name must be of type string.")
        self.__first_name = first_name
        if not isinstance(last_name, str):
            raise ValueError("Last name must be of type string.")
        self.__last_name = last_name
        if not isinstance(passport_number, int):
            raise ValueError("Passport number  must be of type int.")
        self.__passport_number = passport_number

    def set_first_name(self, first_name: str):
        """
        Set the passenger's first name.

        Args:
            first_name (str): The new first name.

        Returns:
            None

        Raises:
            ValueError: If 'first_name' is not a string.
        """
        if not isinstance(first_name, str):
            raise ValueError("First name must be of type string.")
        self.__first_name = first_name

    def set_last_name(self, last_name: str):
        """
        Set the passenger's last name.

        Args:
            last_name (str): The new last name.

        Returns:
            None

        Raises:
            ValueError: If 'last_name' is not a string.
        """
        if not isinstance(last_name, str):
            raise ValueError("Last name must be of type string.")
        self.__last_name = last_name

    def set_passport_number(self, passport_number: int):
        """
        Set the passenger's passport number.

        Args:
            passport_number (int): The new passport number.

        Returns:
            None

        Raises:
            ValueError: If 'passport_number' is not an integer.
        """
        if not isinstance(passport_number, int):
            raise ValueError("Passport number  must be of type int.")
        self.__passport_number = passport_number

    def get_first_name(self) -> str:
        """
        Get the passenger's first name.

        Returns:
            str: The first name of the passenger.
        """
        return self.__first_name

    def get_last_name(self) -> str:
        """
        Get the passenger's last name.

        Returns:
            str: The last name of the passenger.
        """
        return self.__last_name

    def get_passport_number(self) -> int:
        """
        Get the passenger's passport number.

        Returns:
            int: The passport number of the passenger.
        """
        return self.__passport_number

    def __repr__(self):
        return f"Passager(first_name='{self.__first_name}', last_name='{self.__last_name}', passport_number={self.__passport_number})"
