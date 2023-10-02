"""
test_doubly_linked_list.py
"""

import unittest
from src.data_structures.DoublyLinkedList import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    """Test class to test DoublyLinkedList"""

    def setUp(self):
        self.linked_list = DoublyLinkedList[int]()

    def test_append(self):
        """testing append to DoublyLinkedList"""
        self.linked_list.append(1)
        self.assertEqual(str(self.linked_list), "[ 1 ]")

    def test_contains(self):
        """testing contains in DoublyLinkedList"""
        self.assertEqual(self.linked_list.contains(1), False)
        self.linked_list.append(2)
        self.assertEqual(self.linked_list.contains(1), False)
        self.assertEqual(self.linked_list.contains(2), True)

    def test_is_empty(self):
        """testing whether DoublyLinkedList is empty"""
        self.assertEqual(self.linked_list.is_empty(), True)
        self.linked_list.append(1)
        self.assertEqual(self.linked_list.is_empty(), False)

    def test_index_of(self):
        """testing finding index in DoublyLinkedList"""
        for i in range(5):
            self.linked_list.append(i)
        self.assertEqual(self.linked_list.index_of(0), 0)
        self.assertEqual(self.linked_list.index_of(2), 2)
        self.assertEqual(self.linked_list.index_of(4), 4)
        self.assertRaises(ValueError, self.linked_list.index_of, 5)

    def test_insert(self):
        """testing insert to the DoublyLinkedList at a specific index"""
        self.linked_list.append(1)
        self.linked_list.append(3)
        self.linked_list.append(4)

        self.linked_list.insert(0, 5)
        self.assertEqual(str(self.linked_list), "[ 5, 1, 3, 4 ]")

        self.linked_list.insert(2, 6)
        self.assertEqual(str(self.linked_list), "[ 5, 1, 6, 3, 4 ]")

        self.linked_list.insert(4, 7)
        self.assertEqual(str(self.linked_list), "[ 5, 1, 6, 3, 7, 4 ]")

        self.linked_list.insert(-20, 10)
        self.assertEqual(str(self.linked_list), "[ 10, 5, 1, 6, 3, 7, 4 ]")

        self.linked_list.insert(100, 20)
        self.assertEqual(str(self.linked_list), "[ 10, 5, 1, 6, 3, 7, 4, 20 ]")

        self.linked_list.insert(-self.linked_list.length(), 2)
        self.assertEqual(str(self.linked_list),
                         "[ 2, 10, 5, 1, 6, 3, 7, 4, 20 ]")

    def test_length(self):
        """testing length of the DoublyLinkedList"""
        self.assertEqual(self.linked_list.length(), 0)
        self.linked_list.append(1)
        self.assertEqual(self.linked_list.length(), 1)
        self.linked_list.insert(2, 2)
        self.assertEqual(self.linked_list.length(), 2)
        self.linked_list.pop_back()
        self.assertEqual(self.linked_list.length(), 1)
        self.linked_list.remove(1)
        self.assertEqual(self.linked_list.length(), 0)

    def test_pop_back(self):
        """testing pop from DoublyLinkedList"""
        self.assertRaises(IndexError, self.linked_list.pop_back)
        self.assertRaises(IndexError, self.linked_list.pop_back)
        for i in range(5):
            self.linked_list.append(i)
        self.assertEqual(self.linked_list.pop_back(), 4)
        self.assertEqual(self.linked_list.pop_back(), 3)
        self.assertEqual(self.linked_list.pop_back(), 2)

    def test_pop_front(self):
        """testing pop from DoublyLinkedList"""
        self.assertRaises(IndexError, self.linked_list.pop_front)
        self.assertRaises(IndexError, self.linked_list.pop_front)
        for i in range(5):
            self.linked_list.append(i)
        self.assertEqual(self.linked_list.pop_front(), 0)
        self.assertEqual(self.linked_list.pop_front(), 1)
        self.assertEqual(self.linked_list.pop_front(), 2)

    def test_remove(self):
        """testing remove of an element from DoublyLinkedList"""
        self.assertRaises(ValueError, self.linked_list.remove, 5)
        for i in range(5):
            self.linked_list.append(i)
        self.linked_list.append(0)
        self.linked_list.remove(0)
        self.assertEqual(self.linked_list.length(), 5)


if __name__ == "__main__":
    unittest.main()
