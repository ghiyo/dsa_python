"""
BinarySearchTree.py
"""

from copy import deepcopy
from typing import TypeVar, Generic, Optional, List

T = TypeVar('T')


class BST(Generic[T]):
    class _TNode(Generic[T]):
        def __init__(self, value: T) -> None:
            self.value: T = value
            self.left: Optional[BST._TNode[T]] = None
            self.right: Optional[BST._TNode[T]] = None

    def __init__(self) -> None:
        self.root: Optional[BST._TNode[T]] = None

    def _insert_aux(self, node: Optional[_TNode[T]], value: T) -> _TNode[T]:
        """Helper method for insert"""
        if node is None:
            return self._TNode(value)
        elif value < node.value:
            node.left = self._insert_aux(node.left, value)
        elif value > node.value:
            node.right = self._insert_aux(node.right, value)
        return node

    def insert(self, value: T) -> None:
        """Inserts a node in the tree

        Args:
            value (T): item to insert
        """
        self.root = self._insert_aux(self.root, value)
        return

    def _find_aux(self, node: Optional[_TNode[T]], value: T) -> Optional[T]:
        """Helper method for find"""
        if node is None:
            return None
        elif node.value == value:
            return deepcopy(node.value)
        elif node.value < value:
            return self._find_aux(node.right, value)
        elif node.value > value:
            return self._find_aux(node.left, value)

    def find(self, value: T) -> Optional[T]:
        """finds and returns a value in the tree

        Args:
            value (T): found item, None if not found
        """
        return self._find_aux(self.root, value)

    def _successor(self, node: _TNode[T]) -> T:
        """Finds the successor of a node in its right subtree and returns it

        Args:
            node (_TNode[T]): node to search a successor for

        Returns:
            T: value immediately bigger than the node we are searching for
        """
        successor = node.right
        while successor.left:
            successor = successor.left
        return successor.value

    def _predecessor(self, node: _TNode[T]) -> T:
        """Finds the predecessor of a node in its left subtree and returns it

        Args:
            node (_TNode[T]): node to search a predecessor for

        Returns:
            T: value immediately smaller then the node we are searching for
        """
        predecessor = node.left
        while predecessor.right:
            predecessor = predecessor.right
        return predecessor.value

    def _remove_aux(self, node: Optional[_TNode[T]], key: T) -> (bool, _TNode[T]):
        """Helper method for remove"""
        removed = False
        if node is None:
            return removed, node
        elif node.value < key:  # search right subtree
            removed, node.right = self._remove_aux(node.right, key)
        elif node.value > key:  # search left subtree
            removed, node.left = self._remove_aux(node.left, key)
        else:
            removed = True  # we found the node, we can delete it
            if not (node.left or node.right):  # case 1: node if a leaf
                node = None
            # case 2: node has a right child (could have two children but we don't care)
            elif node.right:
                node.value = self._successor(node)
                _, node.right = self._remove_aux(
                    node.right, node.value)  # remove the successor
            else:  # case 3: there is no right child, so we go for left child subtree
                node.value = self._predecessor(node)
                _, node.left = self._remove_aux(
                    node.left, node.value)  # remove the predecessor
        return removed, node

    def remove(self, value: T) -> bool:
        """Removes an element from the tree

        Args:
            value (T): element to remove
        """
        removed, self.root = self._remove_aux(self.root, value)
        return removed

    def _preorder_traversal_aux(self, node, response):
        """Auxiliary function that returns a preordered list of the tree

        Args:
            node (_TNode[T])  : node to process in the tree  
            response (List[T]): preordered list to add to
        """
        if node is None:
            return
        response.append(node.value)
        self._preorder_traversal_aux(node.left, response)
        self._preorder_traversal_aux(node.right, response)

    def preorder_traversal(self) -> List[T]:
        """Returns a preorder arrangement of the tree elements

        Returns:
            List[T]: array of elements in preorder
        """
        response = []
        self._preorder_traversal_aux(self.root, response)
        return response

    def _inorder_traversal_aux(self, node, response):
        """Auxiliary function that returns a inordered list of the tree

        Args:
            node (_TNode[T])  : node to process in the tree  
            response (List[T]): inordered list to add to
        """
        if node is None:
            return
        self._inorder_traversal_aux(node.left, response)
        response.append(node.value)
        self._inorder_traversal_aux(node.right, response)

    def inorder_traversal(self) -> List[T]:
        """Returns an inorder arrangement of the tree elements

        Returns:
            List[T]: array of elements inorder
        """
        response = []
        self._inorder_traversal_aux(self.root, response)
        return response

    def _postorder_traversal_aux(self, node, response):
        """Auxiliary function that returns a postordered list of the tree

        Args:
            node (_TNode[T])  : node to process in the tree  
            response (List[T]): postordered list to add to
        """
        if node is None:
            return
        self._postorder_traversal_aux(node.left, response)
        self._postorder_traversal_aux(node.right, response)
        response.append(node.value)

    def postorder_traversal(self) -> List[T]:
        """Returns a postorder arrangement of the tree elements

        Returns:
            List[T]: array of elements in postorder
        """
        response = []
        self._postorder_traversal_aux(self.root, response)
        return response
