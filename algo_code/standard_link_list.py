class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


"""

    We want this behavior from a LinkedList
    
    insert_at_beginning() --> This needs to keep track of head
    
    [5]
    
    data = 5
    next = None
    
    [10][5]
    
    data = 10
    next = [5]
    
    insert_at_end() --> This needs to go through each element and find the empty one.
    
    [5]
    
    data = 5
    next = None
    
    [5][10]
    
    data = 10
    next = None

"""


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def reveal(self):

        if self.head is None:
            print("LinkedList is empty")
            return

        itr = self.head

        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    # TODO Create a function to find the length of the Linked List
    def __len__(self):
        pass
    # TODO Create a remove function to remove an element at a given index. What is the time complexity for this?

    def remove(self, index):
        pass


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["Welcome", "To", "LinkedList"])
    ll.reveal()
