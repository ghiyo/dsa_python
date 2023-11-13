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

    def _remove_aux(self, parent: Optional[_TNode[T]], node: Optional[_TNode[T]], value: T) -> (bool, _TNode[T]):
        """Helper method for remove"""
        if node is None:
            return False, node
        elif node.value == value:
            # check for parent if it exists
            

    def remove(self, value: T) -> bool:
        """Removes an element from the tree

        Args:
            value (T): element to remove
        """
        removed, self.root = self._remove_aux(None, self.root, value)
        return removed

    def preorder_traversal(self) -> List[T]:
        """Returns a preorder arrangement of the tree elements

        Returns:
            List[T]: array of elements in preorder
        """
        pass

    def inorder_traversal(self) -> List[T]:
        """Returns an inorder arrangement of the tree elements

        Returns:
            List[T]: array of elements inorder
        """
        pass

    def postorder_traversal(self) -> List[T]:
        """Returns a postorder arrangement of the tree elements

        Returns:
            List[T]: array of elements in postorder
        """
        pass
