import unittest
from domain.passager import Passager
from domain.plane import Plane
from repository.plane_repository import PlaneRepository
from controller.plane_controller import PlaneController

class TestPlaneController(unittest.TestCase):

    def setUp(self):
        self.passager1 = Passager("John", "Doe", 123)
        self.passager2 = Passager("Jane", "Smith", 456)
        self.passager3 = Passager("Jake", "Brown", 789)
        self.passager4 = Passager("Jack", "Wilson", 101)
        
        self.plane1 = Plane("1", "CompanyA", 100, "DestinationA", [self.passager1, self.passager2])
        self.plane2 = Plane("2", "CompanyB", 150, "DestinationA", [self.passager3, self.passager4])
        self.plane3 = Plane("3", "CompanyC", 200, "DestinationB", [self.passager1, self.passager2, self.passager3])
        
        self.repo = PlaneRepository([self.plane1, self.plane2, self.plane3])
        self.controller = PlaneController(self.repo)

    def test_sort_by_pass_number(self):
        sorted_planes = self.controller.sort_by_pass_number()
        self.assertEqual(len(sorted_planes), 3)
        self.assertEqual(sorted_planes[0].get_id(), "3")  # plane3 has 3 passengers
        self.assertEqual(len(sorted_planes[0].get_passager_list()), 3)
        self.assertEqual(sorted_planes[2].get_id(), "2")  # plane2 has 2 passengers

    def test_sort_by_passenger_number_first_name(self):
        sorted_planes = self.controller.sort_by_passenger_number_first_name("J")
        self.assertEqual(len(sorted_planes), 3)
        self.assertEqual(sorted_planes[0].get_id(), "3")  # plane2 has 2 J-names
        self.assertTrue(all(p.get_first_name().startswith("J") 
                          for p in sorted_planes[0].get_passager_list()))
        self.assertEqual(len([p for p in sorted_planes[0].get_passager_list()]), 3)

    def test_sort_by_passenget_number_destination(self):
        sorted_planes = self.controller.sort_by_passenget_number_destination()
        self.assertEqual(len(sorted_planes), 3)
        self.assertEqual(sorted_planes[0].get_destination(), "DestinationA")
        self.assertEqual(sorted_planes[1].get_destination(), "DestinationA")
        self.assertEqual(sorted_planes[2].get_destination(), "DestinationB")

    def test_filter_by_passenger_name(self):
        filtered_planes = self.controller.filter_by_passenger_name("John")
        self.assertEqual(len(filtered_planes), 2)
        self.assertTrue(any(p.get_first_name() == "John" for p in filtered_planes[0].get_passager_list()))
        self.assertEqual(filtered_planes[0].get_id(), "1")

    def test_groups_different_last_name(self):
        groups = self.controller.groups_different_last_name(2)
        self.assertTrue("2" in groups)  # plane2 has Wilson and Brown
        self.assertEqual(len(groups["2"]), 1)  # One group of 2 different last names
        self.assertEqual(len(groups["2"][0]), 2)  # Each group has 2 passengers
        last_names = {p.get_last_name() for p in groups["2"][0]}
        self.assertEqual(len(last_names), 2)  # Two different last names

    def test_goupt_by_destination(self):
        groups = self.controller.goupt_by_destination(2)
        self.assertTrue("DestinationA" in groups)
        self.assertTrue("DestinationB" in groups)
        self.assertEqual(len(groups["DestinationA"]), 1)  # One list of groups for DestinationA
        self.assertTrue(isinstance(groups["DestinationA"][0], list))  # Contains a list of groups

    def test_create_plane(self):
        new_plane = Plane("4", "CompanyD", 250, "DestinationC", [self.passager1])
        self.controller.create_plane(new_plane)
        plane = self.controller.get_plane("4")
        self.assertEqual(plane.get_id(), "4")
        self.assertEqual(plane.get_company_name(), "CompanyD")
        self.assertEqual(plane.get_seat_number(), 250)
        self.assertEqual(plane.get_destination(), "DestinationC")
        self.assertEqual(len(plane.get_passager_list()), 1)

    def test_update_plane(self):
        self.controller.update_plane("1", company_name="NewCompanyA", seat_number=120)
        plane = self.controller.get_plane("1")
        self.assertEqual(plane.get_company_name(), "NewCompanyA")
        self.assertEqual(plane.get_seat_number(), 120)

    def test_delete_plane(self):
        self.controller.delete_plane("1")
        with self.assertRaises(ValueError):
            self.controller.get_plane("1")

if __name__ == '__main__':
    unittest.main()
