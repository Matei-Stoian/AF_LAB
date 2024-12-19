import unittest
from domain.passager import Passager
from repository.passager_repository import PassagerRepository


class TestPassagerRepository(unittest.TestCase):

    def setUp(self):
        self.passenger1 = Passager("John", "Doe", 123456)
        self.passenger2 = Passager("Jane", "Smith", 654321)
        self.repo = PassagerRepository([self.passenger1])

    def test_create_passager_valid(self):
        self.repo.create_passager(self.passenger2)
        self.assertEqual(len(self.repo.get_all()), 2)
        self.assertEqual(self.repo.get_all()[1].get_first_name(), "Jane")

    def test_create_passager_duplicate(self):
        with self.assertRaises(ValueError):
            self.repo.create_passager(self.passenger1)

    def test_update_passager_by_first_name(self):
        self.repo.update_passager(check_first_name="John", first_name="Johnny")
        updated_passenger = self.repo.get_passager(123456)
        self.assertEqual(updated_passenger.get_first_name(), "Johnny")

    def test_update_passager_by_passport_number(self):
        self.repo.update_passager(passport_number=123456, last_name="Doe-Smith")
        updated_passenger = self.repo.get_passager(123456)
        self.assertEqual(updated_passenger.get_last_name(), "Doe-Smith")

    def test_update_passager_no_match(self):
        with self.assertRaises(ValueError):
            self.repo.update_passager(check_first_name="Nonexistent", first_name="Test")

    def test_get_passager_valid(self):
        passenger = self.repo.get_passager(123456)
        self.assertEqual(passenger.get_first_name(), "John")

    def test_get_passager_invalid(self):
        with self.assertRaises(ValueError):
            self.repo.get_passager(999999)

    def test_delete_passager_valid(self):
        self.repo.delete(123456)
        self.assertEqual(len(self.repo.get_all()), 0)

    def test_delete_passager_invalid(self):
        with self.assertRaises(ValueError):
            self.repo.delete(999999)

if __name__ == "__main__":
    unittest.main()
