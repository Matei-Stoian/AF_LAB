from mypoint import MyPoint
import unittest

class PointTest(unittest.TestCase):
    def test_get_point(self):
        
        point = MyPoint(1, 2, "red")
        self.assertEqual(point.get_point(), (1, 2))

        
        point = MyPoint(-5, 10, "blue")
        self.assertEqual(point.get_point(), (-5, 10))

        
        with self.assertRaises(Exception) as context:
            MyPoint(3, 4, "pink")  
        self.assertEqual(str(context.exception),"Not a valid color")

    def test_get_color(self):
        
        point = MyPoint(1, 2, "red")
        self.assertEqual(point.get_color(), "red")

        point = MyPoint(-5, 10, "blue")
        self.assertEqual(point.get_color(), "blue")

        point = MyPoint(0, 0, "green")
        self.assertEqual(point.get_color(), "green")

    def test_set_color(self):
        point = MyPoint(1, 2, "red")
        point.set_color("green")
        self.assertEqual(point.get_color(), "green")

        point.set_color("yellow")
        self.assertEqual(point.get_color(), "yellow")

        point.set_color("magenta")
        self.assertEqual(point.get_color(), "magenta")

    def test_set_point(self):
        point = MyPoint(1, 2, "red")
        point.set_point(3, 5)
        self.assertEqual(point.get_point(), (3, 5))

        point.set_point(-7, -8)
        self.assertEqual(point.get_point(), (-7, -8))

        point.set_point(0, 0)
        self.assertEqual(point.get_point(), (0, 0))

    


if __name__ == "__main__":
    unittest.main()
    