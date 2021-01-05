
"""
    This is a standard queue class with standard methods.

    When a queue is initialise, it makes these variables

    1. storage = A list/array to store our queue.
    2. size = Shows how many elements are in the queue.
    3. head = An index of the front of the queue.
    4. tail = An index of rear of the queue.
    5. capacity = The maximum number of elements in the queue.

    Methods

    1. isFull = Return whether the queue is full or not.

    2. Enqueue = Append element into the queue.

    3. Dequeue = Remove queue

    What is the problem with Queue (Linear)?

    Answer
    As you can see, LinearQueue relies on having an index increment but the data is not deletes.
    As the queue gets bigger, the queue will consume lots of memory.

"""


class StandardLinearQueue:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.size = 0
        self.head = 0
        self.tail = 0
        self.capacity = capacity

    # Return if Queue is full or not
    def isFull(self):
        return self.capacity == self.size

    # Enqueue --> insert into queue
    def enqueue(self, data):
        # Checks if the queue is full or not.
        if self.isFull():
            raise  Exception("Queue is Full")

        # Append data to the empty position(tail) of the queue
        self.storage[self.tail] = data
        # Update the tail to the next empty spot
        self.tail += 1
        # Update the size of the queue
        self.size += 1

    # Dequeue --> Pop element from the queue
    def dequeue(self):
        # if there is no element in the queue, then it should not return anything
        if self.size == 0:
            return None
        data = self.storage[self.head]
        # the head move forwards at the data gets dequeue (pop)
        self.head += 1
        # if the head is the same as the tail position, the tail came back to the beginning.
        if self.head == self.tail:
            self.head = 0
            self.tail = 0
        # Every time dequeue happens, the size is reduced by 1
        self.size -= 1
        return data


""" 

    A circular queue is a memory friendly version of LinearQueue where modular is used to define the position of 
    tails and head.
    
    Let's consider this queue
    
    We enqueue 3 times using CiruclarQueue enqueue method, the queue has capacity of 3.
    
    [1][][]
    
    size = 1
    head = 0
    tail = (0 + 1) % 3 = 1

    
    [1][2][]
    
    size = 2
    head = 0
    tail = (1 + 1) % 3 = 2
    
    [1][2][3]
    
    size = 3
    head = 0
    tail = (2 + 1) % 3 = 0
    
    As you can see, the tail is back at the beginning position and ready to insert there.
    
    Let's dequeue(pop) one element
    
    [][2][3]
    
    size = 2
    head = (0 + 1) % 3 = 1
    tail = 0 
    
    Then enqueue one more element
    
    [4][2][3]
    
    size = 3
    head = 1
    tail = (0 + 1) % 3 = 1
    
    Thus, this algorithm forms a CircularQueue so the memory is not wasted.
     
"""


class StandardCircularQueue:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.size = 0
        self.head = 0
        self.tail = 0
        self.capacity = capacity

    # Return if Queue is full or not
    def isFull(self):
        return self.capacity == self.size

    # Enqueue --> insert into queue
    def enqueue(self, data):
        # Checks if the queue is full or not.
        if self.isFull():
            raise  Exception("Queue is Full")

        # Append data to the empty position(tail) of the queue
        self.storage[self.tail] = data
        # Update the tail to the next empty spot --> using modulus to find index for Circular Queue
        self.tail += (self.tail + 1) % self.capacity
        # Update the size of the queue
        self.size += 1

    # Dequeue --> Pop element from the queue
    def dequeue(self):
        # if there is no element in the queue, then it should not return anything
        if self.size == 0:
            return None
        data = self.storage[self.head]
        # the head move forwards at the data gets dequeue (pop) --> using modulus to find index for Circular Queue
        self.head += (self.head + 1) % self.capacity
        # Every time dequeue happens, the size is reduced by 1
        self.size -= 1
        return data
