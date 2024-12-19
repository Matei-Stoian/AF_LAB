import unittest
from myvector import MyVector
from vectorrepository import VectorRepository


class TestVectorRepository(unittest.TestCase):
    def setUp(self):
        """
        Sets up a test case with a VectorRepository and some sample vectors.
        """
        self.repo = VectorRepository()
        self.vector1 = MyVector(name_id=1, color="r", type=1, values=[1, 2, 3])
        self.vector2 = MyVector(name_id="v2", color="b", type=2, values=[4, 5, 6])
        self.repo.add_vector(self.vector1)
        self.repo.add_vector(self.vector2)

    def test_add_vector(self):
        """
        Test the `add_vector` method.
        """
        self.assertEqual(len(self.repo.get_all_vectors()), 2)
        vector3 = MyVector(name_id=3, color="g", type=3, values=[7, 8, 9])
        self.repo.add_vector(vector3)
        self.assertEqual(len(self.repo.get_all_vectors()), 3)
        self.assertIn(vector3, self.repo.get_all_vectors())

    def test_get_all_vectors(self):
        """
        Test the `get_all_vectors` method.
        """
        vectors = self.repo.get_all_vectors()
        self.assertEqual(len(vectors), 2)
        self.assertEqual(vectors[0], self.vector1)
        self.assertEqual(vectors[1], self.vector2)

    def test_get_vector_by_index(self):
        """
        Test the `get_vector_by_index` method.
        """
        self.assertEqual(self.repo.get_vector_by_index(0), self.vector1)
        self.assertEqual(self.repo.get_vector_by_index(1), self.vector2)
        with self.assertRaises(IndexError):
            self.repo.get_vector_by_index(2)

    def test_update_vector_by_index(self):
        """
        Test the `update_vector_by_index` method.
        """
        self.repo.update_vector_by_index(0, name_id="new_id", color="y", vector_type=3)
        updated_vector = self.repo.get_vector_by_index(0)
        self.assertEqual(updated_vector.get_name_id(), "new_id")
        self.assertEqual(updated_vector.get_color(), "y")
        self.assertEqual(updated_vector.get_type(), 3)

    def test_update_vector_by_name_id(self):
        """
        Test the `update_vector_by_name_id` method.
        """
        self.repo.update_vector_by_name_id(check_name_id=1,name_id="updated_id",color="m")
        updated_vector = self.repo.get_vector_by_index(0)
        self.assertEqual(updated_vector.get_name_id(), "updated_id")
        self.assertEqual(updated_vector.get_color(), "m")
        with self.assertRaises(ValueError):
            self.repo.update_vector_by_name_id("nonexistent_id", name_id="new_id")

    def test_delete_vector_by_index(self):
        """
        Test the `delete_vector_by_index` method.
        """
        self.repo.delete_vector_by_index(0)
        self.assertEqual(len(self.repo.get_all_vectors()), 1)
        self.assertEqual(self.repo.get_vector_by_index(0), self.vector2)
        with self.assertRaises(IndexError):
            self.repo.delete_vector_by_index(1)

    def test_delete_vector_by_name_id(self):
        """
        Test the `delete_vector_by_name_id` method.
        """
        self.repo.delete_vector_by_name_id(1)
        self.assertEqual(len(self.repo.get_all_vectors()), 1)
        self.assertEqual(self.repo.get_vector_by_index(0), self.vector2)
        self.repo.delete_vector_by_name_id("v2")
        self.assertEqual(len(self.repo.get_all_vectors()), 0)

    def test_get_sum_of_all_vectors(self):
        """
        Test the `get_sum_of_all_vectors` method.
        """
        total_sum = self.repo.get_sum_of_all__vectors()
        self.assertEqual(total_sum, sum([1, 2, 3, 4, 5, 6]))
        vector3 = MyVector(name_id=3, color="g", type=3, values=[7, 8, 9])
        self.repo.add_vector(vector3)
        self.assertEqual(self.repo.get_sum_of_all__vectors(), total_sum + sum([7, 8, 9]))

    def test_delete_all_vectors(self):
        """
        Test the `delete_all_vectors` method.
        """
        self.repo.delete_all__vectors()
        self.assertEqual(len(self.repo.get_all_vectors()), 0)
        self.assertListEqual(self.repo.get_all_vectors(), [])

    def test_set_color_for_type(self):
        """
        Test the `set_color_for_type` method.
        """
        self.repo.set_color_for_type(1, "g")
        updated_vector = self.repo.get_vector_by_index(0)
        self.assertEqual(updated_vector.get_color(), "g")
        with self.assertRaises(ValueError):
            self.repo.set_color_for_type(1, "invalid_color")
        with self.assertRaises(ValueError):
            self.repo.set_color_for_type(-1, "b")


if __name__ == "__main__":
    unittest.main()
