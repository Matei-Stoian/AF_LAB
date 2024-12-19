import unittest
from domain.passager import Passager
class TestPassager(unittest.TestCase):
    def test_initialization_valid(self):
        passenger = Passager("John", "Doe", 123456)
        self.assertEqual(passenger.get_first_name(), "John")
        self.assertEqual(passenger.get_last_name(), "Doe")
        self.assertEqual(passenger._Passager__passport_number, 123456)  # Accessing private attribute

    def test_initialization_invalid(self):
        with self.assertRaises(ValueError):
            Passager(123, "Doe", 123456)

        with self.assertRaises(ValueError):
            Passager("John", 456, 123456)

        with self.assertRaises(ValueError):
            Passager("John", "Doe", "ABC")

    def test_set_first_name(self):
        passenger = Passager("John", "Doe", 123456)

        passenger.set_first_name("Jane")
        self.assertEqual(passenger.get_first_name(), "Jane")

        with self.assertRaises(ValueError):
            passenger.set_first_name(123)

        self.assertEqual(passenger.get_first_name(), "Jane")

    def test_set_last_name(self):
        passenger = Passager("John", "Doe", 123456)

        
        passenger.set_last_name("Smith")
        self.assertEqual(passenger.get_last_name(), "Smith")

        with self.assertRaises(ValueError):
            passenger.set_last_name(123)

        self.assertEqual(passenger.get_last_name(), "Smith")

    def test_set_passport_number(self):
        passenger = Passager("John", "Doe", 123456)
    
        passenger.set_passport_number(654321)
        self.assertEqual(passenger.get_passport_number(), 654321) 

        with self.assertRaises(ValueError):
            passenger.set_passport_number("ABC")

        self.assertEqual(passenger.get_passport_number(), 654321) 

if __name__ == "__main__":
    unittest.main()
