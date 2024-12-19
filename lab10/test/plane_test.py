import unittest
from domain.passager import Passager
from domain.plane import Plane

class TestPlane(unittest.TestCase):

    def test_initialization_valid(self):
        passenger1 = Passager("John", "Doe", 123456)
        passenger2 = Passager("Jane", "Smith", 654321)
        plane = Plane(1, "Airline", 150, "New York", [passenger1, passenger2])

        self.assertEqual(plane.get_id(), 1)
        self.assertEqual(plane.get_company_name(), "Airline")
        self.assertEqual(plane.get_seat_number(), 150)
        self.assertEqual(plane.get_destination(), "New York")
        self.assertEqual(len(plane.get_passager_list()), 2)

    def test_getters(self):
        passenger = Passager("John", "Doe", 123456)
        plane = Plane("A123", "Delta", 200, "London", [passenger])

        self.assertEqual(plane.get_id(), "A123")
        self.assertEqual(plane.get_company_name(), "Delta")
        self.assertEqual(plane.get_seat_number(), 200)
        self.assertEqual(plane.get_destination(), "London")

    def test_setters_valid(self):
        passenger1 = Passager("John", "Doe", 123456)
        passenger2 = Passager("Jane", "Smith", 654321)
        plane = Plane(1, "Airline", 150, "New York", [passenger1])

        # Test set_id
        plane.set_id("A123")
        self.assertEqual(plane.get_id(), "A123")

        # Test set_company_name
        plane.set_company_name("Delta")
        self.assertEqual(plane.get_company_name(), "Delta")

        # Test set_seat_number
        plane.set_seat_number(300)
        self.assertEqual(plane.get_seat_number(), 300)

        # Test set_destination
        plane.set_destination("London")
        self.assertEqual(plane.get_destination(), "London")

        # Test set_passager_list
        plane.set_passager_list([passenger1, passenger2])
        self.assertEqual(len(plane.get_passager_list()), 2)

    def test_passager_list_modification(self):
        passenger1 = Passager("John", "Doe", 123456)
        passenger2 = Passager("Jane", "Smith", 654321)
        plane = Plane(1, "Airline", 150, "New York", [passenger1])

        # Add a passenger
        passengers = plane.get_passager_list()
        passengers.append(passenger2)
        plane.set_passager_list(passengers)
        self.assertEqual(len(plane.get_passager_list()), 2)
        self.assertEqual(plane.get_passager_list()[1].get_first_name(), "Jane")

        # Remove a passenger
        passengers.pop(0)
        plane.set_passager_list(passengers)
        self.assertEqual(len(plane.get_passager_list()), 1)
        self.assertEqual(plane.get_passager_list()[0].get_first_name(), "Jane")

    def test_invalid_initialization(self):
        # Invalid id
        with self.assertRaises(TypeError):
            Plane(None, "Airline", 150, "New York", [])

        # Invalid company_name
        with self.assertRaises(TypeError):
            Plane(1, None, 150, "New York", [])

        # Invalid seat_number
        with self.assertRaises(TypeError):
            Plane(1, "Airline", "seats", "New York", [])

        # Invalid destination
        with self.assertRaises(TypeError):
            Plane(1, "Airline", 150, None, [])

        # Invalid passengers_list
        with self.assertRaises(TypeError):
            Plane(1, "Airline", 150, "New York", None)

if __name__ == "__main__":
    unittest.main()
