"""
Stack.py
"""

from copy import deepcopy
from typing import Generic, TypeVar, Optional
from ArrayList import ArrayList

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._stack: ArrayList[T] = ArrayList()

    def push(self, item: T) -> None:
        """Push an item on top of the stack

        Args:
            item (T): item to push
        """
        self._stack.append(item)
        return

    def pop(self) -> Optional[T]:
        """Remove and return the top item on the stack

        Returns:
            Optional[T]: Item at the top of the stack, None if stack is empty
        """
        if len(self._stack) == 0:
            return None
        return self._stack.pop()

    def peek(self) -> Optional[T]:
        """Return a copy of the top item in the stack

        Returns:
            Optional[T]: Item at the top of the stack, None if stack is empty
        """
        n = len(self._stack)
        if n == 0:
            return None
        return deepcopy(self._stack[n-1])

    def is_empty(self) -> bool:
        """Check if stack is empty or not

        Returns:
            bool: True/False
        """
        return self._stack.is_empty()

    def size(self) -> int:
        """Returns the size of the stack

        Returns:
            int: size of the stack
        """
        return len(self._stack)
