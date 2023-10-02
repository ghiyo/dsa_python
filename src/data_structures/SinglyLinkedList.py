"""
SinglyLinkedList.py

Implementation of a Singly Linked List
"""


from typing import Generic, TypeVar, Optional

T = TypeVar('T')


class SinglyLinkedList(Generic[T]):
    class _Node(Generic[T]):
        def __init__(self, data: T = None):
            self.data: T = data
            self.next: Optional[SinglyLinkedList._Node[T]] = None

    def __init__(self):
        self._head: Optional[self._Node[T]] = None
        self._size: int = 0

    def __str__(self) -> str:
        if self._size == 0:
            return "[]"
        list_str = "[ "
        current = self._head
        while current.next:
            list_str += str(current.data) + ", "
        list_str = str(current.data) + " ]"
        return list_str

    def __getitem__(self, index: int) -> T:
        if not -self._size-1 < index < self._size:
            raise IndexError("list index out of range")

        if index < 0:
            index = self._size + index

        count = 0
        current = self._head
        while count < index:
            current = current.next
            count += 1

        return current.data

    def __setitem__(self, index: int, value: T) -> None:
        if not -self._size-1 < index < self._size:
            raise IndexError("list index out of range")

        if index < 0:  # handle negative indices
            index = self._size + index

        current = self._head
        while index > 0:
            current = current.next
            index -= 1
        current.data = value

    def append(self, data: T) -> None:
        """Appends an element to the end of the list

        Args:
            data (T): data to append of type T
        """
        node = self._Node(data)
        self._size += 1
        if not self._head:
            self._head = node
            return

        current = self._head
        while current.next:
            current = current.next
        current.next = node

    def insert(self, index: int, data: T) -> None:
        """Inserts an element at a specific index

        Args:
            index (int): index to insert at
            data (T): element to insert with type T
        """
        if index >= self._size:
            index = self._size          # set to end of list
        if index < -self._size:
            index = 0                   # set to beginning
        elif index < 0:
            index = self._size + index  # convert to positive index

        node = self._Node(data)
        self._size += 1
        if index == 0:
            node.next = self._head
            self._head = node
        else:
            previous = None
            current = self._head
            while index > 0:
                previous = current
                current = current.next
                index -= 1
            previous.next = node
            node.next = current

    def remove(self, data: T) -> None:
        """Remove the first occurance of an element

        Args:
            data (T): remove element with type T
        """
        if self._head and self._head.data == data:
            self._head = self._head.next
            self._size -= 1
            return

        previous = None
        current = self._head

        while current:
            if current.data == data:
                previous.next = current.next
                current.next = None
                self._size -= 1
                return
            previous = current
            current = current.next

        # element not found, raise exception
        raise ValueError("list.remove(x): x not in list")

    def pop(self, index: int = -1) -> T:
        """Pop an element at a specific index and return it. 
        Remove last element if no index provided.

        Args:
            index (int, optional): index to remove an element from. Defaults to -1.

        Returns:
            T: Element with type T
        """
        if not -self._size-1 < index < self._size:
            raise IndexError("pop index out of range")

        if index < 0:
            index = self._size + index

        node = self._head
        if index == 0:
            self._head = self._head.next
            node.next = None
        else:
            previous = None
            current = self._head
            while index > 0:
                previous = current
                current = current.next
                index -= 1
            previous.next = current.next
            current.next = None
            node = current

        self._size -= 1
        if self._size == 0:
            self._head = None

        return node.data

    def index(self, data: T) -> int:
        """Return the index of an element

        Args:
            data (T): element to search

        Returns:
            int: index of the element, -1 if not found
        """
        index = 0
        current = self._head
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def contains(self, data: T) -> bool:
        """Check to see if a list contains an element

        Args:
            data (T): Element to search with type T

        Returns:
            bool: True/False
        """
        current = self._head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def length(self) -> int:
        """Returns the length of the list

        Returns:
            int: size of the list
        """
        return self._size

    def is_empty(self) -> bool:
        """Check to see if list is empty or not

        Returns:
            bool: True/False
        """
        return self._size == 0 and not self._head
