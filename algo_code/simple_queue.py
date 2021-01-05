""" Queue ADT and an array implementation.

Defines a generic abstract queue with the usual methods, and implements
a circular queue and linear queue using arrays. It also implements a linked queue.
Also defines UnitTests for the class.
"""
__author__ = "Maria Garcia de la Banda, modified by Brendon Taylor"
__docformat__ = 'reStructuredText'

from abc import ABC, abstractmethod
from enum import Enum
from typing import Generic
# from node import Node
from .referential_array import ArrayR, T


class QueueSpitter:

    has_queue = None
    active_queue = None

    def __init__(self):
        """ Init nothing """

    @classmethod
    def make_queue(cls):
        cls.active_queue = LinearQueue(max_capacity=10)
        cls.active_queue.append(1)
        cls.active_queue.append(2)
        cls.active_queue.append(3)
        cls.active_queue.append(4)
        cls.has_queue = True


class Queue(ABC, Generic[T]):
    """ Abstract class for a generic Queue. """

    def __init__(self) -> None:
        self.length = 0

    @abstractmethod
    def append(self, item: T) -> None:
        """ Adds an element to the rear of the queue."""
        pass

    @abstractmethod
    def serve(self) -> T:
        """ Deletes and returns the element at the queue's front."""
        pass

    def __len__(self) -> int:
        """ Returns the number of elements in the queue."""
        return self.length

    def is_empty(self) -> bool:
        """ True if the queue is empty. """
        return len(self) == 0

    @abstractmethod
    def is_full(self) -> bool:
        """ True if the stack is full and no element can be pushed. """
        pass

    def clear(self):
        """ Clears all elements from the queue. """
        self.length = 0


class LinearQueue(Queue[T]):
    """ Linear implementation of a queue with arrays.

    Attributes:
         length (int): number of elements in the queue (inherited)
         front (int): index of the element at the front of the queue
         rear (int): index of the first empty space at the back of the queue
         array (ArrayR[T]): array storing the elements of the queue

    ArrayR cannot create empty arrays. So MIN_CAPACITY used to avoid this.
    """
    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        Queue.__init__(self)
        self.front = 0
        self.rear = 0
        self.array = ArrayR(max(self.MIN_CAPACITY, max_capacity))

    def append(self, item: T) -> None:
        """ Adds an element to the rear of the queue.
        :pre: queue is not full
        :complexity: O(1)
        :raises Exception: if the queueu is full
        """
        if self.is_full():
            raise Exception("Queue is full")

        self.array[self.rear] = item
        self.length += 1
        self.rear += 1

    def serve(self) -> T:
        """ Deletes and returns the element at the queue's front.
        :pre: queue is not empty
        :complexity: O(1)
        :raises Exception: if the queue is empty
        """
        if self.is_empty():
            raise Exception("Queue is empty")

        self.length -= 1
        item = self.array[self.front]
        self.front += 1
        return item

    def clear(self):
        """ Clears all elements from the queue.
        :complexity: O(1)
        """
        super().clear()
        self.front = 0
        self.rear = 0

    def is_full(self) -> bool:
        """ True if the queue is full and no element can be appended.
        :complexity: O(1)
        """
        return self.rear == len(self.array)

    def __toString__(self):
        """
        :complexity: O(N*M)
            where N is the length of the list
                  M is the size of the biggest item
        """
        result = "["
        for i in range(self.front, self.rear):
            if i >= self.front:
                result += ', '
            result += str(self.array[i])
        result += ']'


class CircularQueue(Queue[T]):
    """ Circular implementation of a queue with arrays.

    Attributes:
         length (int): number of elements in the queue (inherited)
         front (int): index of the element at the front of the queue
         rear (int): index of the first empty space at the back of the queue
         array (ArrayR[T]): array storing the elements of the queue

    ArrayR cannot create empty arrays. So MIN_CAPACITY used to avoid this.
    """
    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        Queue.__init__(self)
        self.front = 0
        self.rear = 0
        self.array = ArrayR(max(self.MIN_CAPACITY, max_capacity))

    def append(self, item: T) -> None:
        """ Adds an element to the rear of the queue.
        :pre: queue is not full
        :complexity: O(1)
        :raises Exception: if the queueu is full
        """
        if self.is_full():
            raise Exception("Queue is full")

        self.array[self.rear] = item
        self.length += 1
        self.rear = (self.rear + 1) % len(self.array)

    def serve(self) -> T:
        """ Deletes and returns the element at the queue's front.
        :pre: queue is not empty
        :complexity: O(1)
        :raises Exception: if the queue is empty
        """
        if self.is_empty():
            raise Exception("Queue is empty")

        self.length -= 1
        item = self.array[self.front]
        self.front = (self.front + 1) % len(self.array)
        return item

    def is_full(self) -> T:
        """ True if the queue is full and no element can be appended.
        :complexity: O(1)
        """
        return len(self) == len(self.array)

    def clear(self) -> None:
        """ Clears all elements from the queue.
        :complexity: O(1)
        """
        Queue.__init__(self)
        self.front = 0
        self.rear = 0

    def __str__(self) -> str:
        """Computes a string from the queue items - front to rear.
        :complexity: O(N*M)
            where N is the length of the list
                  M is the size of the biggest item
        """
        length = len(self)
        if length > 0:
            index = self.front
            output = str(self.array[index])
            for _ in range(len(self) - 1):
                index = (index + 1) % len(self.array)
                output += "," + str(self.array[index])
        else:
            output = ""
        return output


# class LinkQueue(Queue[T]):
#     """ Linked implementation of a queue with nodes.
#
#     Attributes:
#          length (int): number of elements in the linked queue (inherited)
#          front (int): reference to the front node (None represents an empty queue)
#          rear (int): reference to the rear node (None represents an empty queue)
#     """
#
#     def __init__(self, _=None) -> None:
#         Queue.__init__(self)
#         self.front = None
#         self.rear = None
#
#     def clear(self) -> None:
#         """ Resets the queue
#         :complexity: O(1)
#         """
#         super().clear()
#         self.front = None
#         self.rear = None
#
#     def is_full(self) -> bool:
#         """ Returns true if the list is full
#         :complexity: O(1)
#         """
#         return False
#
#     def append(self, item: T) -> None:
#         """ Adds an element to the rear of the queue.
#         :complexity: O(1)
#         """
#         new_node = Node(item)
#         if self.is_empty():
#             self.front = new_node
#         else:
#             self.rear.next = new_node
#         self.rear = new_node
#         self.length += 1
#
#     def serve(self) -> T:
#         """ Deletes and returns the element at the queue's front.
#         :pre: queue is not empty
#         :complexity: O(1)
#         :raises Exception: if the queue is empty
#         """
#         if self.is_empty():
#             raise Exception("Queue is empty")
#
#         temp = self.front.item
#         self.front = self.front.next
#         self.length -= 1
#         if self.is_empty():
#             self.rear = None
#         return temp
#
#     def __toString__(self):
#         """ Computes a string from the queue items - front to rear.
#         :complexity: O(N*M)
#             where N is the length of the list
#                   M is the size of the biggest item
#         """
#         result = ""
#         node = self.front
#         while node is not None:
#             result += str(node.item) + ", "
#             node = node.next
#
#         return result
