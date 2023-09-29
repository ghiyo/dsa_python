"""
test_array_list.py
"""

import unittest
from src.data_structures.ArrayList import ArrayList


class TestArrayList(unittest.TestCase):
    """Test class to test ArrayList"""

    def setUp(self):
        self.array_list = ArrayList[int]()

    def test_append(self):
        """testing append to ArrayList"""
        self.array_list.append(1)
        self.assertEqual(self.array_list[0], 1)

    def test_capacity_increase(self):
        """testing clear on ArrayList"""
        initial_capacity = 10
        self.array_list = ArrayList[int](initial_capacity)

        for i in range(initial_capacity * 2):
            self.array_list.append(i)
        self.assertEqual(len(self.array_list), initial_capacity * 2)

    def test_clear(self):
        """testing clear on ArrayList"""
        self.array_list.append(1)
        self.array_list.clear()
        self.assertEqual(len(self.array_list), 0)

    def test_copy(self):
        """testing copy from ArrayList"""
        for i in range(10):
            self.array_list.append(i)
        copied = self.array_list.copy()
        self.assertIsNot(self.array_list, copied)
        self.assertEqual(self.array_list, copied)

    def test_count(self):
        """testing element count in ArrayList"""
        for i in range(5):
            self.array_list.append(i)

        self.assertEqual(self.array_list.count(5), 0)
        self.assertEqual(self.array_list.count(4), 1)

        self.array_list.append(4)

        self.assertEqual(self.array_list.count(4), 2)

    def test_extend(self):
        """testing extend on ArrayList from ArrayList"""
        elements_num = 5
        for i in range(elements_num):
            self.array_list.append(i)

        new_array = ArrayList[int]()

        for j in range(elements_num):
            new_array.append(j)

        self.array_list.extend(new_array)
        self.assertEqual(len(self.array_list), elements_num*2)

    def test_is_empty(self):
        """testing whether ArrayList is empty"""
        self.assertEqual(self.array_list.is_empty(), True)
        self.array_list.append(1)
        self.assertEqual(self.array_list.is_empty(), False)

    def test_index(self):
        """testing finding index in ArrayList"""
        for i in range(5):
            self.array_list.append(i)
        self.assertEqual(self.array_list.index(0), 0)
        self.assertEqual(self.array_list.index(2), 2)
        self.assertEqual(self.array_list.index(4), 4)
        self.assertEqual(self.array_list.index(5), -1)

    def test_insert(self):
        """testing insert to the ArrayList at a specific index"""
        self.array_list.append(1)
        self.array_list.append(3)
        self.array_list.append(4)

        self.array_list.insert(0, 5)
        self.assertEqual(self.array_list[0], 5)

        self.array_list.insert(2, 6)
        self.assertEqual(self.array_list[2], 6)

        self.array_list.insert(4, 7)
        self.assertEqual(self.array_list[4], 7)

        self.array_list.insert(-20, 10)
        self.assertEqual(self.array_list[0], 10)

        self.array_list.insert(100, 20)
        self.assertEqual(self.array_list[len(self.array_list)-1], 20)

        self.array_list.insert(-len(self.array_list), 2)
        self.assertEqual(self.array_list[0], 2)

    def test_pop(self):
        """testing pop from ArrayList"""
        self.assertRaises(IndexError, self.array_list.pop)
        self.assertRaises(IndexError, self.array_list.pop, 5)
        for i in range(5):
            self.array_list.append(i)
        self.assertEqual(self.array_list.pop(0), 0)
        self.assertEqual(self.array_list.pop(len(self.array_list)-1), 4)
        self.assertEqual(self.array_list.pop(1), 2)

    def test_remove(self):
        """testing remove of an element from ArrayList"""
        self.assertRaises(ValueError, self.array_list.remove, 5)
        for i in range(5):
            self.array_list.append(i)
        self.array_list.append(0)
        self.array_list.remove(0)
        self.assertEqual(len(self.array_list), 5)


if __name__ == "__main__":
    unittest.main()
