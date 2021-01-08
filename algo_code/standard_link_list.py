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

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # TODO Create a function to find the length of the Linked List
    def __len__(self):

        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    # TODO Create a remove function to remove an element at a given index. What is the time complexity for this?

    def remove(self, index):

        count = 0
        temp = self.head

        while temp.next is not None:
            if count == index-1:
                temp.next = temp.next.next
                break
            temp = temp.next
            count += 1
    # TODO Create a copy function to copy the LinkedList (THIS QUESTION IS VERY DIFFICULT IN EXAM)

    def copy(self):

        copy = LinkedList()
        temp = self.head
        current_copy = None
        while temp is not None:
            if current_copy is None:
                copy.head = Node(temp.data)
                current_copy = copy.head
            else:
                current_copy.next = Node(temp.data)
                current_copy = current_copy.next
            temp = temp.next

    # TODO: Recursively copy the list :)

    def aux_copy(self):
        copy = LinkedList()

        copy.head = self.copy_rec(self.head)
        return copy

    def copy_rec(self, head):

        # base case
        if head is None:
            return head

        node = Node(head.data)
        node.next = self.copy_rec(head.next)
        return node


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["Welcome", "To"])
    ll.reveal()
    b = ll.aux_copy()
    b.reveal()

