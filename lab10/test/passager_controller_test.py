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

    def test_filter_by_first_last_name(self):
        filtered_passagers = self.controller.filter_by_first_last_name("John")
        self.assertEqual(len(filtered_passagers), 1)
        self.assertEqual(filtered_passagers[0].get_first_name(), "John")

    def test_create_passager(self):
        new_passager = Passager("Jack", "Brown", 101)
        self.controller.create_passager(new_passager)
        passager = self.controller.get_passager(101)
        self.assertEqual(passager.get_first_name(), "Jack")
        self.assertEqual(passager.get_last_name(), "Brown")
        self.assertEqual(passager.get_passport_number(), 101)

    def test_update_passager(self):
        self.controller.update_passager(passport_number=123, first_name="Johnny")
        passager = self.controller.get_passager(123)
        self.assertEqual(passager.get_first_name(), "Johnny")

    def test_delete_passager(self):
        self.controller.delete_passager(123)
        with self.assertRaises(ValueError):
            self.controller.get_passager(123)

  

if __name__ == '__main__':
    unittest.main()
