"""
AVTTree.py
"""

from copy import deepcopy
from typing import TypeVar, Generic, Optional, List

T = TypeVar('T')


class AVL(Generic[T]):

    class _AVLNode(Generic[T]):
        def __init__(self, value: T) -> None:
            self.value: T = value
            self.left: Optional[AVL._AVLNode[T]] = None
            self.right: Optional[AVL._AVLNode[T]] = None
            self.height: int = 0

    def __init__(self):
        self.root: Optional[AVL._AVLNode[T]] = None

    def insert(self, value: T) -> None:
        """Inserts a value into the AVL tree, maintaining the AVL invariant.

        Args:
            value (T): value to insert
        """
        pass

    def delete(self, value: T) -> bool:
        """Deletes a value in the AVL tree, maintaining the AVL invariant.

        Args:
            value (T): value to delete

        Returns:
            bool: whether the target value was deleted or not
        """
        pass

    def find(self, value: T) -> Optional[T]:
        """Finds and returns a copy of node value containing 'value' in the AVL tree.

        Args:
            value (T): value to search for.

        Returns:
            Optional[T]: copy of value found or none if not found.
        """
        pass

    def _rotate_left(self, node: _AVLNode[T]) -> _AVLNode[T]:
        """Performs a left notation given a node

        Args:
            node (_AVLNode[T]): parent node to do a rotation on

        Returns:
            _AVLNode[T]: the new node after the rotation
        """
        pass

    def _rotate_right(self, node: _AVLNode[T]) -> _AVLNode[T]:
        """Performs a right notation given a node

        Args:
            node (_AVLNode[T]): parent node to do a rotation on

        Returns:
            _AVLNode[T]: the new node after the rotation
        """
        pass

    def _rebalance(self, node: _AVLNode[T]) -> _AVLNode[T]:
        """Rebalances a subtree in the AVL tree to maintain the AVL invariant.

        Args:
            node (_AVLNode[T]): root node of the subtree to do the rebalancing from

        Returns:
            _AVLNode[T]: the new root node of the subtree that was rebalanced
        """
        pass

    def _successor(self, node: _AVLNode[T]) -> T:
        """Given a node finds the successor of it in the subtree

        Args:
            node (_AVLNode[T]): node to find a successor to

        Returns:
            T: value of the successor node
        """
        pass

    def _predecessor(self, node: _AVLNode[T]) -> T:
        """Given a node finds the predecessor of it in the subtree

        Args:
            node (_AVLNode[T]): node to find a predecessor to

        Returns:
            T: value of the predecessor node
        """
        pass

    def successor(self, value: T) -> Optional[T]:
        """Given a value finds the successor to it if one exists

        Args:
            value (T): value to search a successor for

        Returns:
            Optional[T]: value of the successor if found, none otherwise
        """
        pass

    def predecessor(self, value: T) -> Optional[T]:
        """Given a value finds the predecessor to it if one exists

        Args:
            value (T): value to search a predecessor for

        Returns:
            Optional[T]: value of the predecessor if found, none otherwise
        """
        pass

    def preorder_traversal(self) -> List[T]:
        """Returns a preorder arrangement of the tree elements

        Returns:
            List[T]: array of elements in preorder
        """
        pass

    def inorder_traversal(self) -> List[T]:
        """Returns a inorder arrangement of the tree elements

        Returns:
            List[T]: array of elements in inorder
        """
        pass

    def postorder_traversal(self) -> List[T]:
        """Returns a postorder arrangement of the tree elements

        Returns:
            List[T]: array of elements in postorder
        """
        pass

    def is_balanced(self) -> bool:
        """Checks to see if the AVL tree is balanced

        Returns:
            bool: true if balanced, false otherwise
        """
        pass

    def minimum(self) -> Optional[T]:
        """Finds the minimum value in the tree

        Returns:
            Optional[T]: minimum value if tree is not empty, none otherwise
        """
        pass

    def maximum(self) -> Optional[T]:
        """Finds the maximum value in the tree

        Returns:
            Optional[T]: maximum value if tree is not empty, none otherwise
        """
        pass

    def height(self) -> int:
        """Returns the height of the tree

        Returns:
            int: height of the tree
        """
        pass
