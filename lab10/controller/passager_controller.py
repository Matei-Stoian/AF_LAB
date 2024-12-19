from domain.passager import Passager
from repository.passager_repository import PassagerRepository

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
        return filter(passagers, lambda x: x.get_first_name() == name or x.get_last_name() == name)
