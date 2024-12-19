import unittest
from myvector import MyVector
import numpy as np


class TestMyVector(unittest.TestCase):

    def setUp(self):
        self.vector1 = MyVector(1, "r", 1, [1, 2, 3])
        self.vector2 = MyVector(2, "g", 1, [4, 5, 6])

    def test_initialization(self):
        vec = MyVector("id", "b", 2, [10, 20, 30])
        self.assertEqual(vec.get_name_id(), "id")
        self.assertEqual(vec.get_color(), "b")
        self.assertEqual(vec.get_type(), 2)
        self.assertEqual(vec.get_values(), [10, 20, 30])
        self.assertTrue(isinstance(vec.get_values(), list))

        with self.assertRaises(ValueError):
            MyVector("id", "z", 2, [10, 20, 30])

        with self.assertRaises(ValueError):
            MyVector("id", "r", 0, [10, 20, 30])

    def test_get_name_id(self):
        self.assertEqual(self.vector1.get_name_id(), 1)
        self.assertEqual(self.vector2.get_name_id(), 2)
        self.assertNotEqual(self.vector1.get_name_id(), self.vector2.get_name_id())

    def test_get_color(self):
        self.assertEqual(self.vector1.get_color(), "r")
        self.assertEqual(self.vector2.get_color(), "g")
        self.assertIn(self.vector1.get_color(), ["r", "g", "b"])

    def test_get_type(self):
        self.assertEqual(self.vector1.get_type(), 1)
        self.assertEqual(self.vector2.get_type(), 1)
        self.assertTrue(self.vector1.get_type() > 0)

    def test_get_values(self):
        self.assertEqual(self.vector1.get_values(), [1, 2, 3])
        self.assertEqual(self.vector2.get_values(), [4, 5, 6])
        self.assertEqual(len(self.vector1.get_values()), 3)

    def test_set_name_id(self):
        self.vector1.set_name_id("new_id")
        self.assertEqual(self.vector1.get_name_id(), "new_id")

        with self.assertRaises(ValueError):
            self.vector1.set_name_id([])

        self.assertNotEqual(self.vector1.get_name_id(), self.vector2.get_name_id())

    def test_set_color(self):
        self.vector1.set_color("b")
        self.assertEqual(self.vector1.get_color(), "b")

        with self.assertRaises(ValueError):
            self.vector1.set_color("z")

        self.assertNotEqual(self.vector1.get_color(), self.vector2.get_color())

    def test_set_type(self):
        self.vector1.set_type(5)
        self.assertEqual(self.vector1.get_type(), 5)

        with self.assertRaises(ValueError):
            self.vector1.set_type(0)

        self.assertNotEqual(self.vector1.get_type(), self.vector2.get_type())

    def test_set_values(self):
        self.vector1.set_values([10, 20, 30])
        self.assertEqual(self.vector1.get_values(), [10, 20, 30])

        with self.assertRaises(ValueError):
            self.vector1.set_values([10, "20", 30])

        self.assertNotEqual(self.vector1.get_values(), self.vector2.get_values())

    def test_add_scalar(self):
        self.vector1.add_scalar(5)
        self.assertEqual(self.vector1.get_values(), [6, 7, 8])

        self.vector1.add_scalar(-3)
        self.assertEqual(self.vector1.get_values(), [3, 4, 5])

        self.assertEqual(len(self.vector1.get_values()), 3)

    def test_add(self):
        self.vector1 + self.vector2
        self.assertEqual(self.vector1.get_values(), [5, 7, 9])
        self.assertEqual(self.vector1.get_color(), "r")
        self.assertEqual(len(self.vector1.get_values()), len(self.vector2.get_values()))

    def test_sub(self):
        self.vector2 - self.vector1
        self.assertEqual(self.vector2.get_values(), [3, 3, 3])
        self.assertTrue(all(isinstance(i, int) for i in self.vector2.get_values()))

    def test_mul(self):
        result = self.vector1 * self.vector2
        self.assertEqual(result, 32)
        self.assertTrue(isinstance(result, int))
        self.assertGreater(result, 0)

    def test_get_sum(self):
        self.assertEqual(self.vector1.get_sum(), 6)
        self.assertEqual(self.vector2.get_sum(), 15)
        self.assertGreater(self.vector2.get_sum(), self.vector1.get_sum())

    def test_get_product(self):
        self.assertEqual(self.vector1.get_product(), 6)
        self.assertEqual(self.vector2.get_product(), 120)
        self.assertNotEqual(self.vector1.get_product(), self.vector2.get_product())

    def test_get_avg(self):
        self.assertEqual(self.vector1.get_avg(), 2)
        self.assertEqual(self.vector2.get_avg(), 5)
        self.assertLess(self.vector1.get_avg(), self.vector2.get_avg())

    def test_get_min(self):
        self.assertEqual(self.vector1.get_min(), 1)
        self.assertEqual(self.vector2.get_min(), 4)
        self.assertTrue(self.vector1.get_min() < self.vector2.get_min())

    def test_get_max(self):
        self.assertEqual(self.vector1.get_max(), 3)
        self.assertEqual(self.vector2.get_max(), 6)
        self.assertGreater(self.vector2.get_max(), self.vector1.get_max())


if __name__ == "__main__":
    unittest.main()
