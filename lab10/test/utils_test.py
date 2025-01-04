import unittest
from utils.utils import quick_sort, filter, form_k_groups

class TestUtils(unittest.TestCase):

    def test_quick_sort(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_nums = quick_sort(nums)
        self.assertEqual(sorted_nums, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

        nums = ["apple", "orange", "banana", "pear"]
        sorted_nums = quick_sort(nums)
        self.assertEqual(sorted_nums, ["apple", "banana", "orange", "pear"])

        nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_nums = quick_sort(nums, comp=lambda x, y: x > y)
        self.assertEqual(sorted_nums, [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1])

    def test_filter(self):
        nums = [1, 2, 3, 4, 5, 6]
        filtered_nums = filter(nums, key=lambda x: x % 2 == 0)
        self.assertEqual(filtered_nums, [2, 4, 6])

        words = ["apple", "banana", "cherry", "date"]
        filtered_words = filter(words, key=lambda x: "a" in x)
        self.assertEqual(filtered_words, ["apple", "banana", "date"])

    def test_form_k_groups(self):
        source = [1, 2, 3, 4]
        groups = form_k_groups(2, source)
        self.assertEqual(groups, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])

        source = ["apple", "banana", "cherry"]
        groups = form_k_groups(2, source)
        self.assertEqual(groups, [["apple", "banana"], ["apple", "cherry"], ["banana", "cherry"]])

        source = [1, 2, 3]
        groups = form_k_groups(3, source)
        self.assertEqual(groups, [[1, 2, 3]])

if __name__ == '__main__':
    unittest.main()
