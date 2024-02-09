"""
test_array_list.py
"""

import unittest
from src.data_structures.BinarySearchTree import BST


class TestBinarySearchTree(unittest.TestCase):
    """Test class to test BinarySearchTree"""

    def setUp(self):
        self.bst = BST[int]()

    def test_insert(self):
        """testing insert to BinarySearchTree"""
        test_nodes = [5, 3, 7, 2, 1, 4, 8, 6]
        for i in test_nodes:
            self.bst.insert(i)
        self.assertEqual(self.bst.preorder_traversal(),
                         [5, 3, 2, 1, 4, 7, 6, 8])

    def test_remove(self):
        """testing the remove in BinarySearchTree"""
        test_nodes = [5, 3, 7, 2, 1, 4, 8, 6]
        for i in test_nodes:
            self.bst.insert(i)
        self.assertEqual(self.bst.remove(5), True)
        self.assertEqual(self.bst.preorder_traversal(), [6, 3, 2, 1, 4, 7, 8])
        self.assertEqual(self.bst.remove(9), False)
        self.assertEqual(self.bst.preorder_traversal(), [6, 3, 2, 1, 4, 7, 8])
        self.assertEqual(self.bst.remove(1), True)
        self.assertEqual(self.bst.preorder_traversal(), [6, 3, 2, 4, 7, 8])
        self.assertEqual(self.bst.remove(7), True)
        self.assertEqual(self.bst.preorder_traversal(), [6, 3, 2, 4, 8])
        self.assertEqual(self.bst.remove(3), True)
        self.assertEqual(self.bst.preorder_traversal(), [6, 4, 2, 8])

    def test_preorder_traversal(self):
        """testing the preorder_traversal in BinarySearchTree"""
        test_nodes = [5, 3, 7, 2, 1, 4, 8, 6]
        for i in test_nodes:
            self.bst.insert(i)
        self.assertEqual(self.bst.preorder_traversal(),
                         [5, 3, 2, 1, 4, 7, 6, 8])

    def test_inorder_traversal(self):
        """testing the inorder_traversal in BinarySearchTree"""
        test_nodes = [5, 3, 7, 2, 1, 4, 8, 6]
        for i in test_nodes:
            self.bst.insert(i)
        self.assertEqual(self.bst.inorder_traversal(),
                         [1, 2, 3, 4, 5, 6, 7, 8])

    def test_postorder_traversal(self):
        """testing the postorder_traversal in BinarySearchTree"""
        test_nodes = [5, 3, 7, 2, 1, 4, 8, 6]
        for i in test_nodes:
            self.bst.insert(i)
        self.assertEqual(self.bst.postorder_traversal(),
                         [1, 2, 4, 3, 6, 8, 7, 5])


if __name__ == "__main__":
    unittest.main()
