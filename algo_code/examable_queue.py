class Queue:

    def __init__(self, capacity):

        self.array = [None] * capacity
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

    def __resize__(self):

        # Double array size
        temp_array = [None] * (len(self.array) * 2)
        # print(temp_array)

        index = self.front
        temp_array_index = 0

        for i in range(self.count):
            temp_array[temp_array_index] = self.array[index]
            index = (index + 1) % len(self.array)
            # print(str(temp_array) + " " + str(index))
            # print(self.array[index])
            temp_array_index = temp_array_index + 1
        # When full, the rear = 0, we increase the rear up to where it was.
        self.rear = len(self.array)
        self.front = 0
        self.array = temp_array

    def serve(self):

        assert self.count > 0, "Array is empty"

        item = self.array[self.front]

        self.front = (self.front + 1) % len(self.array)

        self.count = self.count - 1

        return item

    def __str__(self):

        str_to_concat = ""

        for i in range(self.front, self.rear):

            if i == self.front:

                str_to_concat = str_to_concat + str(self.array[i]) + ", "

            elif i == self.rear:

                str_to_concat = str_to_concat + str(self.array[i])

            else:

                str_to_concat = str_to_concat + str(self.array[i])

            return_string = "[" + str_to_concat + "]"

        return return_string


q = Queue(3)
q.append(10)
q.append(20)
q.serve()
q.serve()
q.append(30)
q.append(40)
print(q.array)
print(q.front)
print(q.count)