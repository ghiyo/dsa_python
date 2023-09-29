"""
ArrayList.py

Contains an implementation of an ArrayList or dynamic array.
"""

from __future__ import annotations
import copy
from typing import Iterator, List, Type, TypeVar, Generic, Final

T = TypeVar('T')


class ArrayList(Generic[T]):
    """Resizable array that increases in capacity"""

    DEFAULT_CAPACITY: Final = 2

    def __init__(self, capacity=DEFAULT_CAPACITY) -> None:
        self._capacity: int = capacity
        self._size: int = 0
        self._data: List[T] = [None] * self._capacity

    def __getitem__(self, index: int) -> T:
        if not -self._size-1 < index < self._size:
            raise IndexError("ArrayList index out of range")
        return self._data[index]

    def __len__(self) -> int:
        return self._size

    def __eq__(self, other: ArrayList[T]):
        if self._size != len(other):
            return False
        for i in range(self._size):
            if self._data[i] != other[i]:
                return False
        return True

    def __setitem__(self, index: int, value: T) -> None:
        if not -self._size-1 < index < self._size:
            raise IndexError("ArrayList index out of range")
        self._data[index] = value

    def __str__(self) -> str:
        if self._size == 0:
            return "[]"
        array_str = "["
        for i in range(self._size-1):
            array_str += str(self._data[i]) + ", "
        array_str += str(self._data[self._size-1]) + "]"
        return array_str

    def __contains__(self, value: T) -> bool:
        for i in range(self._size):
            if self._data[i] == value:
                return True
        return False

    def __iter__(self) -> Iterator[T]:
        for i in range(self._size):
            yield self._data[i]

    def append(self, value: T) -> None:
        """Adds an element to the end of the ArrayList

        Args:
            value (T): element to be added
        """

        self._data[self._size] = value
        self._size += 1

        if self._size == self._capacity:
            self._resize(self._size + self._size // 2)

    def clear(self) -> None:
        """Clears the ArrayList and resets the capacity"""
        self._size = 0
        self._capacity = self.DEFAULT_CAPACITY
        self._data = [None] * self._capacity

    def copy(self) -> ArrayList[T]:
        """Generates a copy of the ArrayList

        Returns:
            ArrayList[T]: Copy of the ArrayList
        """
        return copy.deepcopy(self)

    def count(self, value: T) -> int:
        """Returns the count of an element in the ArrayList

        Args:
            value (T): element to look up

        Returns:
            int: count of the element in ArrayList
        """
        count = 0
        for i in range(self._size):
            if self._data[i] == value:
                count += 1
        return count

    def extend(self, iterable: ArrayList[T]) -> None:
        """Extends the ArrayList with another ArrayList

        Args:
            iterable (ArrayList[T]): ArrayList to copy from
        """
        for data in iterable:
            self.append(data)

    def is_empty(self) -> bool:
        """Checks to see if the ArrayList is empty

        Returns:
            bool: True or False
        """
        return self._size == 0

    def index(self, value: T) -> int:
        """Finds and returns the location of the first occurence of an element

        Args:
            value (T): Element to look up

        Returns:
            int: index of the first occurence, -1 if not found
        """
        for i in range(self._size):
            if self._data[i] == value:
                return i
        return -1

    def insert(self, index: int, value: T) -> None:
        """Inserts an element at the specified index

        Args:
            index (int): index to insert at
            value (T): element to insert
        """
        if index >= self._size:
            index = self._size

        if index < -self._size:  # if index negative convert to positive
            index = 0
        elif index < 0:
            index = self._size + index

        # Shift elements to the right after the index
        for i in range(self._size-1, index, -1):
            self._data[i] = self._data[i-1]

        self._data[index] = value
        self._size += 1

        if self._size == self._capacity:
            self._resize(self._size + self._size // 2)

    def pop(self, index=-1) -> T:
        """Pops an element at specified index and returns it

        Args:
            index (int, optional): Index to remove element from. Defaults to -1.

        Returns:
            T: Element at the index
        """
        if self._size == 0:
            raise IndexError("pop from empty ArrayList")
        if not -self._size-1 < index < self._size:
            raise IndexError("ArrayList index out of range")

        if index < 0:  # if index negative convert to the positive version of the index
            index = self._size + index

        value = self._data[index]

        # Shift elements to the left of where the value was
        for i in range(index, self._size, 1):
            self._data[i] = self._data[i+1]
        self._size -= 1

        # Resize if array size is less than 25% of the capacity
        if self._size < self._capacity // 4:
            self._resize(max(self._size + self._size //
                         2, self.DEFAULT_CAPACITY))

        return value

    def remove(self, value: T) -> None:
        """Removes the first occurence of the element from ArrayList

        Args:
            value (T): Element to remove
        """
        index = -1

        for i in range(self._size):
            if self._data[i] == value:
                index = i
                break

        # if value found remove at that index and shift to the left
        if index != -1:
            for i in range(index, self._size, 1):
                self._data[i] = self._data[i+1]
            self._size -= 1
        else:
            raise ValueError("Value not in ArrayList")

        if self._size < self._capacity // 4:
            self._resize(max(self._size + self._size //
                         2, self.DEFAULT_CAPACITY))

    def _resize(self, new_capacity: int) -> None:
        self._capacity = new_capacity
        new_data = [None] * self._capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
