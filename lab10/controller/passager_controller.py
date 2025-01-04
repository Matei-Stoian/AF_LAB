from domain.passager import Passager
from repository.passager_repository import PassagerRepository
from utils.utils import filter
class PassagerController:
    def __init__(self, passager_repo: PassagerRepository):
        """
        Initialize the controller with a passenger repository.

        Args:
            passager_repo (PassagerRepository): The repository managing Passager instances.

        Returns:
            None

        Raises:
            None
        """
        self.__repo = passager_repo

    def sort_passager_by_last_name(self):
        """
        Sort passengers by their last name in ascending order.

        Returns:
            list[Passager]: A list of passengers sorted by last name.

        Raises:
            None
        """
        passagers = self.__repo.get_all()
        return sorted(passagers, key=lambda x: x.get_last_name())
    
    def filter_by_first_last_name(self, name: str):
        """
        Filter passengers by first or last name.

        Args:
            name (str): The name to filter by.

        Returns:
            list[Passager]: A list of passengers whose first or last name matches 'name'.

        Raises:
            None
        """
        passagers = self.__repo.get_all()
        return filter(passagers, key= lambda x: x.get_first_name() == name)

    def create_passager(self, passager: Passager):
        """
        Create a new passenger and add it to the repository.

        Args:
            passager (Passager): The passenger to add.

        Returns:
            None

        Raises:
            ValueError: If a passenger with the same passport number already exists.
        """
        self.__repo.create_passager(passager)

    def update_passager(self, check_first_name: str | None = None, passport_number: int | None = None,
                        first_name: str | None = None, last_name: str | None = None):
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
        self.__repo.update_passager(check_first_name, passport_number, first_name, last_name)

    def get_all_passagers(self) -> list[Passager]:
        """
        Retrieve all passengers in the repository.

        Returns:
            list[Passager]: A list of all passengers.

        Raises:
            None
        """
        return self.__repo.get_all()

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
        return self.__repo.get_passager(passport_number)

    def delete_passager(self, passport_number: int):
        """
        Delete a passenger by passport number.

        Args:
            passport_number (int): The passport number of the passenger to delete.

        Returns:
            None

        Raises:
            ValueError: If no passenger is found with the specified passport number.
        """
        self.__repo.delete(passport_number)
