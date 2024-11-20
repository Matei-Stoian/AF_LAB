import unittest
from math import isclose
from mypoint import MyPoint
from pointrepository import PointRepository


class TestPointRepository(unittest.TestCase):
    def test_add_point(self):
        repository = PointRepository()
        repository.addPoint(MyPoint(1, 2, "red"))
        repository.addPoint(MyPoint(3, 4, "blue"))

        all_points = repository.getAllPoints()
        self.assertEqual(len(all_points), 2)
        self.assertEqual(all_points[0].get_point(), (1, 2))
        self.assertEqual(all_points[1].get_color(), "blue")

    def test_remove_points_from_square(self):
        repository = PointRepository()
        repository.addPoint(MyPoint(1, 4, "red"))
        repository.addPoint(MyPoint(3, 3, "blue"))
        repository.addPoint(MyPoint(5, 5, "green"))
        repository.addPoint(MyPoint(2, 1, "yellow"))

        repository.removePointsFromSquare((1,4), 3)
        remaining_points = repository.getAllPoints()

        self.assertEqual(len(remaining_points), 2)
        self.assertIn(MyPoint(5, 5, "green"), remaining_points)
        self.assertIn(MyPoint(1, 4, "red"), remaining_points)

    def test_get_max_dist(self):
        repository = PointRepository()
        repository.addPoint(MyPoint(1, 1, "red"))
        repository.addPoint(MyPoint(4, 5, "blue"))
        repository.addPoint(MyPoint(7, 1, "green"))

        max_dist = repository.getMaxDist()
        self.assertTrue(isclose(max_dist, 6.0))  # Example assertion based on expected behavior

        repository.addPoint(MyPoint(10, 10, "yellow"))
        repository.addPoint(MyPoint(0, 0, "magenta"))

        max_dist = repository.getMaxDist()
        self.assertTrue(isclose(max_dist, 14.14, abs_tol=0.01))  # Adjust this value as per implementation

    def test_shift_points_y(self):
        repository = PointRepository()
        repository.addPoint(MyPoint(1, 2, "red"))
        repository.addPoint(MyPoint(3, 4, "blue"))
        repository.addPoint(MyPoint(5, 6, "green"))

        repository.shiftPointsY()
        points = repository.getAllPoints()

        for point in points:
            self.assertEqual(point.get_x(), 0)

    def test_delete_all_inside_circle(self):
        repository = PointRepository()
        repository.addPoint(MyPoint(1, 1, "red"))
        repository.addPoint(MyPoint(3, 3, "blue"))
        repository.addPoint(MyPoint(5, 5, "green"))
        repository.addPoint(MyPoint(0, 0, "blue"))

        repository.deleteAllInsideCircle(MyPoint(3, 3, "blue"), 3)
        remaining_points = repository.getAllPoints()

        self.assertEqual(len(remaining_points), 1)
        self.assertEqual(remaining_points[0].get_point(), (0, 0))

        repository.addPoint(MyPoint(6, 6, "yellow"))
        repository.deleteAllInsideCircle(MyPoint(6, 6, "yellow"), 2)
        self.assertEqual(len(repository.getAllPoints()), 1)

        repository.deleteAllInsideCircle(MyPoint(0, 0, "magenta"), 10)
        self.assertEqual(len(repository.getAllPoints()), 0)


if __name__ == "__main__":
    unittest.main()
