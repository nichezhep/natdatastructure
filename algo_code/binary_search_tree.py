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

    def len_aux(self, current):

        if current is None:
            return 0

        else:
            return 1 + self.len_aux(current.left) + self.len_aux(current.right)

    def insert(self, item):

        self.root = self.insert_aux(self.root, item)

    def insert_aux(self, current, item):

        # set
        if current is None:
            current = Node(item)

        elif current.item > item:
            current.left = self.insert_aux(current.left, item)

        elif current.item < item:
            current.right = self.insert_aux(current.right, item)

        else:
            raise ValueError("The value is a duplicate.")

        return current

    def get_height(self):

        return self.get_height_aux(self.root)

    def get_height_aux(self, current):

        if current is None:
            return -1

        else:
            return max(self.get_height_aux(current.left), self.get_height_aux(current.right)) + 1

    def inorder(self, f):

        self.inorder_aux(self.root, f)

    def inorder_aux(self, current, f):

        if current is not None:
            self.inorder_aux(current.left, f)
            f(current)
            self.inorder_aux(current.right, f)

    def postorder(self, f):

        self.postorder_aux(self.root, f)

    def postorder_aux(self, current, f):

        if current is not None:
            self.postorder_aux(current.left, f)
            self.postorder_aux(current.right, f)
            f(current)

    def is_balance(self):

        current = self.root
        left_height = self.get_height_aux(current.left)
        right_height = self.get_height_aux(current.right)
        diff_height = abs(left_height - right_height)
        if diff_height >= 2:
            return False
        else:
            return True


def show_item(current):

    print(current.item)

tree = BinaryTree()
tree.insert(10)
tree.insert(2)
tree.insert(1)
tree.insert(9)
tree.insert(11)
tree.insert(13)
tree.insert(12)
tree.insert(14)
tree.insert(15)

tree.postorder(show_item)
print(tree.is_balance())
