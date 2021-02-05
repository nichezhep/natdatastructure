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

    def get_max(self):

        if self.root is None:
            raise ValueError("Heap is empty")
        elif self.root.right is None:
            temp = self.root.item
            self.root = self.root.left
            return temp
        else:
            return self.get_max_aux(self.root.right, self.root)

    def get_max_aux(self, current, parent):
        if current.right is None:
            parent.right = current.left
            return current.item
        else:
            return self.get_max_aux(current.right, current)

    def sum_all(self):

        return self.sum_all_aux(self.root)

    def sum_all_aux(self, current):

        if current is None:

            return 0

        else:

            sum_all_left = self.sum_all_aux(current.left)
            sum_all_right = self.sum_all_aux(current.right)

            sum_node = sum_all_left + sum_all_right

            return sum_node + current.item

    def sum_heq(self, item):
        return self.sum_heq_aux(self.root, item)

    def sum_heq_aux(self, current, item):
        if current is None:
            return 0
        else:

            high_sum = self.sum_heq_aux(current.right, item)

            if current.item == item:
                return high_sum + item
            elif current.item > item:
                return high_sum + current.item + self.sum_heq_aux(current.left, item)
            else:
                return high_sum

    def sum_parents_tail(self, value):

        return self.sum_parents_tail_aux(self.root, value, 0)

    def sum_parents_tail_aux(self, current, value, acc):

        if current is None:
            return None
        elif current.item == value:
            return acc
        else:
            if current.item > value:
                acc = acc + current.item
                return self.sum_parents_tail_aux(current.left, value, acc)
            else:
                acc = acc + current.item
                return self.sum_parents_tail_aux(current.right, value, acc)

    def inorder_iteration(self):

        stack = []

        current = self.root

        while True:

            if current is not None:

                stack.append(current)

                current = current.left

            elif stack:

                current = stack.pop()

                print(current.item)

                current = current.right

            else:

                break

    def peek(self, stack):
        if len(stack) > 0:
            return stack[-1] # -1 means last item on the list
        return None

    def postorder_iteration(self):

        stack = []

        current = self.root

        while True:

            while current:

                if current.right is not None:

                    stack.append(current.right)

                stack.append(current)

                current = current.left

            current = stack.pop()

            if current.right is not None and self.peek(stack) == current.right:
                print("The current after pop is " + str(current.item))
                item = stack.pop()
                print("I have popped: " + str(item.item))
                stack.append(current)
                print("I append this back: " + str(current.item))
                current = current.right
                print("No current is " + str(current.item))
            else:

                print(current.item)
                current = None

            if len(stack) <= 0:
                break


def show_item(current):

    print(current.item)

tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(11)
tree.insert(2)
tree.insert(6)


#tree.postorder(show_item)

tree.postorder_iteration()