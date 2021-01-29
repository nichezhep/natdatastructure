"""

    This is a very standard heap implementation based on 2085 lectures.

    However, we will be using list with blocked position 0, to simulate Array R.

    Note that we need an extra cell in the array
    – If our heap has 10 elements, we use indices 1..10 to store them
    • Thus, we need an array of 11 cells


"""


class Heap:

    def __init__(self, capacity):

        self.array = [None] * (capacity + 1)
        # Set the index 0 as unused to simulate Array R
        self.array[0] = "Unused"
        self.length = 0

    def __len__(self):
        return self.length

    def is_full(self):
        return self.length + 1 == len(self.array)

    def swap(self, index_parent, index_child):

        temp_child = self.array[index_child]
        temp_parent = self.array[index_parent]

        self.array[index_parent] = temp_child
        self.array[index_child] = temp_parent

    def rise(self, k):

        while k > 1 and self.array[k] > self.array[k//2]:
            self.swap(k, k//2)
            k = k//2

    def add(self, element) -> bool:
        """
        Swaps elements while rising
        """
        has_space_left = not self.is_full()

        if has_space_left:
            self.length += 1
            self.array[self.length] = element
            self.rise(self.length)

        return has_space_left

    """
        Swap root with most bottom right element
        Remove that element.
        White heap order is broken,
            sink, swap out the largest child.
    
    """

    def get_max(self):

        max = self.array[1]

        self.swap(1, self.length)
        del self.array[self.length]
        self.length = self.length - 1

        self.sink(1)

        return max

    def largest_child(self, k):
        """ Check also for k having only one child. """

        if 2 * k == self.length or self.array[2 * k] > self.array[2 * k + 1]:
            return 2 * k
        else:
            return 2 * k + 1

    def sink(self, k: int) -> None:
        while 2*k <= self.length:
            child = self.largest_child(k)
            if self.array[k] >= self.array[child]:
                break
            self.swap(child,k)
            k = child

h = Heap(10)
h.add(15)
h.add(20)
h.add(30)
h.add(16)
h.add(50)
h.add(40)

print(h.get_max())
print(h.array)