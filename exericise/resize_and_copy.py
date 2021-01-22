def build_array(size):

    return [None] * size


class Queue:

    def __init__(self, capacity):

        self.array = build_array(capacity)
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.count = 0

    def is_full(self):

        return False

    def is_empty(self):

        return self.count == 0

    def __len__(self):

        return self.count

    def append(self, new_item):

        if self.count == len(self.array):
            self.__resize__()
        self.array[self.rear] = new_item
        self.rear = (self.rear + 1) % len(self.array)
        self.count += 1

    def __resize__ ( self ):
        # Step 1 - Create Temporary Array
        temp_array = build_array(len(self.array) * 2)
        # Step 2 - Define iterative means for real array
        index = self.front
        # Step 3 - Define iterative means for temp array
        index_new_array = 0
        # Step 4 - For Loop
        for _ in range(self.count):
            # As of queue, we do not care about what is already out, we only care about what's in front
            temp_array[index_new_array] = self.array[index]
            # Iterate index through a circular queue
            index = (index + 1) % len(self.array)
            # Iterate temp index to the next one
            index_new_array += 1
        # Set front
        self.front = 0
        # Set rear
        self.rear = len(self.array)
        self.array = temp_array
        self.capacity = len(self.array)

    def serve(self):

        # Make use of the current empty function
        assert not self.is_empty(), " Queue is empty "

        item = self.array[self.front]
        # Dealing Circularity
        self.front = (self.front + 1) % len(self.array)
        # Count goes down by one
        self.count -= 1

        return item

    def __str__(self):
        # Define where front is
        index = self.front

        ans = " "

        for _ in range(self.count):
            ans += (str(self.array[index]) + ' , ')
            index = (index + 1) % len(self.array)

        return ans


