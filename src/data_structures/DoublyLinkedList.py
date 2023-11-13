"""
DoublyLinkedList.py
"""

from copy import deepcopy
from typing import Generic, TypeVar, Optional

T = TypeVar('T')


class DoublyLinkedList(Generic[T]):

    class _Node(Generic[T]):
        def __init__(self, value: T = None) -> None:
            self.value: T = value
            self.next: Optional[DoublyLinkedList._Node[T]] = None
            self.prev: Optional[DoublyLinkedList._Node[T]] = None

    def __init__(self) -> None:
        self._head: Optional[DoublyLinkedList._Node[T]] = None
        self._rear: Optional[DoublyLinkedList._Node[T]] = None
        self._size: int = 0

    def __str__(self) -> str:
        if self._size == 0:
            return "[]"

        list_str = "[ "
        current = self._head
        while current.next:
            list_str += str(current.value) + ", "
            current = current.next
        list_str += str(current.value) + " ]"

        return list_str

    def append(self, value: T) -> None:
        """Add an element to the rear of the list

        Args:
            value (T): element to be added
        """
        node = self._Node(value)
        self._size += 1

        if self._head is None and self._rear is None:
            self._head = self._rear = node
            return

        self._rear.next = node
        node.prev = self._rear
        self._rear = node
        return

    def prepend(self, value: T) -> None:
        """Add an element to the head of the list

        Args:
            value (T): element to be added
        """
        node = self._Node(value)
        self._size += 1

        if self._head is None and self._rear is None:
            self._head = self._rear = node
            return

        self._head.prev = node
        node.next = self._head
        self._head = node
        return

    def get(self, index: int) -> T:
        """Gets the element at the provided index

        Args:
            index (int): index of element

        Returns:
            T: copy of element returned
        """
        if not -self._size <= index < self._size:
            raise IndexError("list index out of range")

        if index < 0:
            index = self._size + index

        current = self._head
        while index > 0:
            current = current.next
            index -= 1

        return deepcopy(current.value)

    def insert(self, index: int, value: T) -> None:
        """Add element at a specified index

        Args:
            index (int): index to add the element at
            value (T): element to be added
        """
        node = self._Node(value)

        if self._head is None and self._rear is None:
            self._head = self._rear = node

        elif index >= self._size:  # insert at rear
            self._rear.next = node
            node.prev = self._rear
            self._rear = node

        elif index <= -self._size or index == 0:  # insert at head
            self._head.prev = node
            node.next = self._head
            self._head = node
        else:
            if index < 0:
                index = self._size + index

            previous = None
            current = self._head
            while index > 0:
                previous = current
                current = current.next
                index -= 1

            node.next = current
            node.prev = previous
            current.prev = previous.next = node

        self._size += 1
        return

    def remove(self, value: T) -> None:
        """Remove an element from the list

        Args:
            value (T): element to be removed
        """
        # 1 element head and rear same
        # element is same as head
        # more than 1 element, if found remove
        # otherwisae throw exception

        if self._head and self._head is self._rear and self._head.value == value:
            self._head = self._rear = None
            self._size -= 1
            return

        if self._head and self._head.value == value:
            self._head = self._head.next
            self._size -= 1
            return

        previous = None
        current = self._head

        while current:
            if current.value == value and current is self._rear:
                previous.next = self._rear.next
                self._rear = previous
                self._size -= 1
                break
            if current.value == value:
                previous.next = current.next
                current.next.prev = previous
                self._size -= 1
                break
            previous = current
            current = current.next

        raise ValueError("list.remove(x): x not in list")

    def pop_front(self) -> T:
        """Remove and return the element at the head

        Returns:
            T: element to be returned
        """
        if self._size == 0:
            raise IndexError("pop_front from an empty list")

        value = self._head.value
        self._size -= 1

        if self._head is self._rear:
            self._head = self._rear = None
        else:
            self._head = self._head.next

        return value

    def pop_back(self) -> T:
        """Remove and return the element at the rear

        Returns:
            T: element to be removed
        """
        if self._size == 0:
            raise IndexError("pop_back from and empty list")

        value = self._rear.value
        self._size -= 1

        if self._head is self._rear:
            self._head = self._rear = None
        else:
            self._rear = self._rear.prev

        return value

    def index_of(self, value: T) -> int:
        """Find and return the index of an element

        Args:
            value (T): element to search for

        Returns:
            int: index to return
        """
        current = self._head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1

        raise ValueError("{} is not in list".format(value))

    def contains(self, value: T) -> bool:
        """Check to see if element is in list

        Args:
            value (T): element to search for

        Returns:
            bool: True/False
        """
        current = self._head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def is_empty(self) -> bool:
        """Check to see if list is empty

        Returns:
            bool: True/False
        """
        return self._size == 0 and self._head is None and self._rear is None

    def length(self) -> int:
        """Return the size of the list

        Returns:
            int: size of the list
        """
        return self._size
