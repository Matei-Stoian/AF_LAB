import unittest
from domain.passager import Passager
from repository.passager_repository import PassagerRepository
from controller.passager_controller import PassagerController

class TestPassagerController(unittest.TestCase):

    def setUp(self):
        self.passager1 = Passager("John", "Doe", 123)
        self.passager2 = Passager("Jane", "Smith", 456)
        self.passager3 = Passager("Jake", "Doe", 789)
        self.repo = PassagerRepository([self.passager1, self.passager2, self.passager3])
        self.controller = PassagerController(self.repo)

    def test_sort_passager_by_last_name(self):
        sorted_passagers = self.controller.sort_passager_by_last_name()
        self.assertEqual(len(sorted_passagers), 3)
        self.assertEqual(sorted_passagers[0].get_last_name(), "Doe")
        self.assertEqual(sorted_passagers[1].get_last_name(), "Doe")
        self.assertEqual(sorted_passagers[2].get_last_name(), "Smith")

    def test_identify_passagers_first_name(self):
        similar_passagers = self.controller.identify_passagers_first_name()
        self.assertEqual(len(similar_passagers), 0)

        passager4 = Passager("Jack", "Brown", 101)
        self.repo.create_passager(passager4)
        similar_passagers = self.controller.identify_passagers_first_name()
        self.assertEqual(len(similar_passagers), 2)
        self.assertEqual(similar_passagers[0].get_first_name(), "Jake")
        self.assertEqual(similar_passagers[1].get_first_name(), "Jack")

if __name__ == '__main__':
    unittest.main()
