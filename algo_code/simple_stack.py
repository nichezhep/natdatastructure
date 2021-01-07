
"""

This Spitter class controls the stack class output
"""


class StackSpitter:

    has_stack = False
    active_stack = None

    def __init__(self):
        """ Init nothing """

    @classmethod
    def make_stack(cls, elems):
        cls.active_stack = SimpleStackStarter(elems=elems)
        cls.active_stack.create_stack()
        cls.has_stack = True


"""

This StackClass shows how simple stack can be
"""


class SimpleStackStarter:

    def __init__(self, elems):

        self.elems = elems
        self.stack = []

    def create_stack(self):

        for i in range(0, self.elems, 1):

            self.stack.append(i)

        return True

    def pop(self):

        return self.stack.pop()

    def push(self, item):

            self.stack.append(item)

    def reveal(self):

        return self.stack

    def __len__(self):

        count = 0
        for i in self.stack:
            count += 1
        return count






