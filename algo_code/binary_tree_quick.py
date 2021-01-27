class Node:

    def __init__(self, item):

        self.item = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):

        self.root = None

    def __len__(self):

        return self.len_aux(self.root)

    def is_balance(self):

        if abs(self.get_height_aux(self.root.left) - self.get_height_aux(self.root.right)) > 1:
            return False
        else:
            return True


    def get_height(self):

        return self.get_height_aux(self.root)

    def get_height_aux(self, current):

        if current is None:
            return - 1
        else:
            return 1 + max(self.get_height_aux(current.left), self.get_height_aux(current.right))

    def len_aux(self, current):

        if current is None:
            return 0
        else:
            return 1 + self.len_aux(current.left) + self.len_aux(current.right)

    def insert(self, item):
        self.root = self.insert_aux(self.root, item)

    def insert_aux(self, current, item):

        if current is None:
            current = Node(item)
        elif item < current.item:
            current.left = self.insert_aux(current.left, item)
        elif item > current.item:
            current.right = self.insert_aux(current.right, item)
        else:
            raise ValueError("Duplicate entry, please choose other number")

        return current

    def preorder(self, f):

        self.preorder_aux(self.root, f)

    def preorder_aux(self, current, f):

        if current is not None:
            f(current)
            self.preorder_aux(current.left, f)
            self.preorder_aux(current.right, f)


def show_item(current):

    print(current.item)

bt = BinaryTree()
bt.insert(10)
bt.insert(2)
bt.insert(1)
bt.insert(9)
bt.insert(11)
bt.insert(12)
bt.insert(13)
bt.insert(14)


print(bt.is_balance())