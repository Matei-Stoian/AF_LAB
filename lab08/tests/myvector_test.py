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
        self.assertEqual(vec.get_values().tolist(), [10, 20, 30])

        with self.assertRaises(ValueError):
            MyVector("id", "z", 2, [10, 20, 30])  

        with self.assertRaises(ValueError):
            MyVector("id", "r", 0, [10, 20, 30])  

    
    def test_get_name_id(self):
        self.assertEqual(self.vector1.get_name_id(), 1)
        self.assertEqual(self.vector2.get_name_id(), 2)

    
    def test_get_color(self):
        self.assertEqual(self.vector1.get_color(), "r")
        self.assertEqual(self.vector2.get_color(), "g")

    
    def test_get_type(self):
        self.assertEqual(self.vector1.get_type(), 1)
        self.assertEqual(self.vector2.get_type(), 1)

    
    def test_get_values(self):
        self.assertEqual(self.vector1.get_values().tolist(), [1, 2, 3])
        self.assertEqual(self.vector2.get_values().tolist(), [4, 5, 6])

    
    def test_set_name_id(self):
        self.vector1.set_name_id("new_id")
        self.assertEqual(self.vector1.get_name_id(), "new_id")

        with self.assertRaises(ValueError):
            self.vector1.set_name_id([])  

    
    def test_set_color(self):
        self.vector1.set_color("b")
        self.assertEqual(self.vector1.get_color(), "b")

        with self.assertRaises(ValueError):
            self.vector1.set_color("z")  

    
    def test_set_type(self):
        self.vector1.set_type(5)
        self.assertEqual(self.vector1.get_type(), 5)

        with self.assertRaises(ValueError):
            self.vector1.set_type(0)  

    
    def test_set_values(self):
        self.vector1.set_values([10, 20, 30])
        self.assertEqual(self.vector1.get_values(), [10, 20, 30])

        with self.assertRaises(ValueError):
            self.vector1.set_values([10, "20", 30])  

    
    def test_add_scalar(self):
        self.vector1.add_scalar(5)
        self.assertEqual(self.vector1.get_values(), [6, 7, 8])

        self.vector1.add_scalar(-3)
        self.assertEqual(self.vector1.get_values(), [3, 4, 5])

    
    def test_add(self):
        self.vector1 + self.vector2
        self.assertEqual(self.vector1.get_values().tolist(),[5, 7, 9])
        self.assertEqual(self.vector1.get_color(), "r")  

    
    def test_sub(self):
        self.vector2 - self.vector1
        self.assertEqual(self.vector2.get_values().tolist() , [3, 3, 3])

    
    def test_mul(self):
        result = self.vector1 * self.vector2
        self.assertEqual(result, 32)  

    
    def test_get_sum(self):
        self.assertEqual(self.vector1.get_sum(), 6)
        self.assertEqual(self.vector2.get_sum(), 15)

    
    def test_get_product(self):
        self.assertEqual(self.vector1.get_product(), 6)  
        self.assertEqual(self.vector2.get_product(), 120)  

    
    def test_get_avg(self):
        self.assertEqual(self.vector1.get_avg(), 2)  
        self.assertEqual(self.vector2.get_avg(), 5)  

    
    def test_get_min(self):
        self.assertEqual(self.vector1.get_min(), 1)
        self.assertEqual(self.vector2.get_min(), 4)

    
    def test_get_max(self):
        self.assertEqual(self.vector1.get_max(), 3)
        self.assertEqual(self.vector2.get_max(), 6)

if __name__ == '__main__':
    unittest.main()
