"""
Stack.py
"""

from copy import deepcopy
from typing import Generic, TypeVar, Optional
from DoublyLinkedList import DoublyLinkedList

T = TypeVar('T')


class Queue(Generic[T]):
    def __init__(self) -> None:
        self._queue: DoublyLinkedList[T] = DoublyLinkedList()

    def enqueue(self, item: T) -> None:
        """Add an item on to the end of queue

        Args:
            item (T): item to push
        """
        self._queue.append(item)
        return

    def dequeue(self) -> Optional[T]:
        """Remove an item from the beginning of the queue

        Returns:
            Optional[T]: Item at the front of the queue, None if queue is empty
        """
        if self._queue.length() == 0:
            return None
        return self._queue.pop_front()

    def peek(self) -> Optional[T]:
        """Return a copy of the top item in the stack

        Returns:
            Optional[T]: Item at the front of the queue, None if queue is empty
        """
        n = len(self._queue)
        if n == 0:
            return None
        return self._queue.get(0)

    def is_empty(self) -> bool:
        """Check if stack is empty or not

        Returns:
            bool: True/False
        """
        return self._queue.is_empty()

    def size(self) -> int:
        """Returns the size of the stack

        Returns:
            int: size of the stack
        """
        return len(self._queue)
