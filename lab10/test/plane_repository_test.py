import unittest
from domain.plane import Plane
from repository.plane_repository import PlaneRepository

class TestPlaneRepository(unittest.TestCase):

    def setUp(self):
        self.repo = PlaneRepository()
        self.plane1 = {
            "plane_id": 1,
            "company_name": "Airline A",
            "seat_number": 200,
            "destination": "Paris",
            "passengers_list": []
        }
        self.plane2 = {
            "plane_id": 2,
            "company_name": "Airline B",
            "seat_number": 150,
            "destination": "London",
            "passengers_list": []
        }

    def test_create_plane(self):
        self.repo.create_plane(**self.plane1)
        self.assertEqual(len(self.repo.get_all_planes()), 1)
        self.assertEqual(self.repo.get_plane(1).get_company_name(), "Airline A")
        self.assertEqual(self.repo.get_plane(1).get_destination(), "Paris")

        with self.assertRaises(ValueError):
            self.repo.create_plane(**self.plane1)  # Duplicate plane ID

    def test_update_plane(self):
        self.repo.create_plane(**self.plane1)
        self.repo.update_plane(1, company_name="Updated Airline", destination="Berlin")

        plane = self.repo.get_plane(1)
        self.assertEqual(plane.get_company_name(), "Updated Airline")
        self.assertEqual(plane.get_destination(), "Berlin")

        with self.assertRaises(ValueError):
            self.repo.update_plane(99, company_name="Non-existent Airline")  # Invalid plane ID

    def test_get_all_planes(self):
        self.repo.create_plane(**self.plane1)
        self.repo.create_plane(**self.plane2)
        all_planes = self.repo.get_all_planes()

        self.assertEqual(len(all_planes), 2)
        self.assertEqual(all_planes[0].get_id(), 1)
        self.assertEqual(all_planes[1].get_id(), 2)

    def test_get_plane(self):
        self.repo.create_plane(**self.plane1)
        plane = self.repo.get_plane(1)

        self.assertEqual(plane.get_company_name(), "Airline A")
        self.assertEqual(plane.get_seat_number(), 200)

        with self.assertRaises(ValueError):
            self.repo.get_plane(99)  # Non-existent plane ID

    def test_delete_plane(self):
        self.repo.create_plane(**self.plane1)
        self.repo.create_plane(**self.plane2)

        self.repo.delete_plane(1)
        self.assertEqual(len(self.repo.get_all_planes()), 1)
        self.assertEqual(self.repo.get_all_planes()[0].get_id(), 2)

        with self.assertRaises(ValueError):
            self.repo.delete_plane(1)  # Plane already deleted

if __name__ == "__main__":
    unittest.main()
