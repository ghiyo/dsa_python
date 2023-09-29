"""
test_singly_linked_list.py
"""

import unittest
from src.data_structures.SinglyLinkedList import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):
    """Test class to test SinglyLinkedList"""

    def setUp(self):
        self.linked_list = SinglyLinkedList[int]()

    def test_append(self):
        """testing append to SinglyLinkedList"""
        self.linked_list.append(1)
        self.assertEqual(self.linked_list[0], 1)

    def test_contains(self):
        """testing contains in SinglyLinkedList"""
        self.assertEqual(self.linked_list.contains(1), False)
        self.linked_list.append(2)
        self.assertEqual(self.linked_list.contains(1), False)
        self.assertEqual(self.linked_list.contains(2), True)

    def test_is_empty(self):
        """testing whether SinglyLinkedList is empty"""
        self.assertEqual(self.linked_list.is_empty(), True)
        self.linked_list.append(1)
        self.assertEqual(self.linked_list.is_empty(), False)

    def test_index(self):
        """testing finding index in SinglyLinkedList"""
        for i in range(5):
            self.linked_list.append(i)
        self.assertEqual(self.linked_list.index(0), 0)
        self.assertEqual(self.linked_list.index(2), 2)
        self.assertEqual(self.linked_list.index(4), 4)
        self.assertEqual(self.linked_list.index(5), -1)

    def test_insert(self):
        """testing insert to the SinglyLinkedList at a specific index"""
        self.linked_list.append(1)
        self.linked_list.append(3)
        self.linked_list.append(4)

        self.linked_list.insert(0, 5)
        self.assertEqual(self.linked_list[0], 5)

        self.linked_list.insert(2, 6)
        self.assertEqual(self.linked_list[2], 6)

        self.linked_list.insert(4, 7)
        self.assertEqual(self.linked_list[4], 7)

        self.linked_list.insert(-20, 10)
        self.assertEqual(self.linked_list[0], 10)

        self.linked_list.insert(100, 20)
        self.assertEqual(self.linked_list[self.linked_list.length()-1], 20)

        self.linked_list.insert(-self.linked_list.length(), 2)
        self.assertEqual(self.linked_list[0], 2)

    def test_length(self):
        """testing length of the SinglyLinkedList"""
        self.assertEqual(self.linked_list.length(), 0)
        self.linked_list.append(1)
        self.assertEqual(self.linked_list.length(), 1)
        self.linked_list.insert(2, 2)
        self.assertEqual(self.linked_list.length(), 2)
        self.linked_list.pop()
        self.assertEqual(self.linked_list.length(), 1)
        self.linked_list.remove(1)
        self.assertEqual(self.linked_list.length(), 0)

    def test_pop(self):
        """testing pop from SinglyLinkedList"""
        self.assertRaises(IndexError, self.linked_list.pop)
        self.assertRaises(IndexError, self.linked_list.pop, 5)
        for i in range(5):
            self.linked_list.append(i)
        self.assertEqual(self.linked_list.pop(0), 0)
        self.assertEqual(self.linked_list.pop(self.linked_list.length()-1), 4)
        self.assertEqual(self.linked_list.pop(1), 2)

    def test_remove(self):
        """testing remove of an element from SinglyLinkedList"""
        self.assertRaises(ValueError, self.linked_list.remove, 5)
        for i in range(5):
            self.linked_list.append(i)
        self.linked_list.append(0)
        self.linked_list.remove(0)
        self.assertEqual(self.linked_list.length(), 5)


if __name__ == "__main__":
    unittest.main()
