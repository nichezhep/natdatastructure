# Factorial Iterative approach
def factorial(number):

    if number == 0:
        return 1

    result = 1

    for i in range(1, number + 1):

        result = result * i

    return result


""" How does factorial work?

    Factorial works by sequentially multiply the numbers up to the given number.
    
    For example, 5! = 5 * 4 * 3 * 2 * 1
    
    When working with recursion, you will need to have ONE function in there to cancel out the operation.
    
    For factorial, your order of recursion goes like this.
    
    fact(5)
    
    Here is the order or return, you can often think about recursion as a stack.
    
    1. 5 * fact(5 - 1) = 120 (BOTTOM STACK)
    2. 4 * fact(4 - 1) = 24
    3. 3 * fact(3 - 1) = 6
    4. 2 * fact(2 - 1) = 2
    5. 1                     (TOP STACK)
    
    So what stopped the recursion?
    
"""


def fact(n):

    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


""" 

    Double recursion call and why we do it?
    
    Recursion can be used to divide problem into smaller chunks to solve it.
    
    For example, a manager can assign his worker to do his stuffs.

    Python Knowledge

    A colon on the left side of an index means everything before, but not including, the index.
    
    list = [1,2,3,4]
    list[:2} = [1, 2]
    
    A colon on the right side of an index means everything after the specified index, including the index
    
    list[2:] = [3, 4]

"""


def lazy_delivery(locations):

    if len(locations) == 1:

        location = locations[0]

        print("Sent package to: " + location)

    else:

        mid = len(locations) // 2
        a = locations[:mid]
        b = locations[mid:]

        print("Task: " + str(mid))

        lazy_delivery(a)
        lazy_delivery(b)


# addresses = ['Company A', 'Company B', 'Company C', 'Company D']
# lazy_delivery(addresses)

# TODO: Draw a graph to represent how this work and how it using flask.

# Exam Question


def has_next(a_list, current_index):
    try:
        a_list[current_index + 1]
    except IndexError:
        return False
    return True


def set_item(some_list, index, item):

    some_list[index] = item


# Badly implemented Zeroed
def zeroed(a_list):
    try:
        count = 0
        while has_next(a_list, count):

            if a_list[count] < 0:
                set_item(a_list, count + 1, 0)
            count += 1
    except IndexError:
        print("STOP ITERATION ERROR!!!")
        pass


# Recursive Zeroed
def zeroed_res(some_list):
    zeroed_aux(some_list, 0)


def zeroed_aux(some_list, index):

    try:
        if some_list[index] < 0:
            set_item(some_list, index, 0)
            index += 1
        else:
            index += 1
        zeroed_aux(some_list, index)
    except IndexError:
        print("STOP ITERATION ERROR!!!")
        pass


if __name__ == '__main__':
    a_list = [-1, 2, 3, -4, 5, -6, -1, -1, -1, -1, -1, -1]
    zeroed_res(a_list)
    print(a_list)






