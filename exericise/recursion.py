"""

    You boss is a bad programmer and wants you to create a recursive function to sum all the number in the list.

    You are badly paid programmer and cannot change job so you will have to do it.

    He gives you an iterative function that you will have to convert.

    He also give you has_next() function to check if there is a next element in the list (How nice of him :))

"""


def sum_all(some_list):

    sum_number = 0

    for i in some_list:

        sum_number += i

    return sum_number


# He is nice enough to give you has_next function.
def has_next(some_list, index):
    try:
        a = some_list[index + 1]
        return True
    except IndexError:
        return False

# TODO: Create a recursive function to sum all of the number in the list.


"""

    Here are exercises for recursion, you will need to transform iterative functions into recursive function.

    Exercise 2 - Binary Search

    BSA Rules

    1. A BSA will only work when its run against a SORTED LISTt.
    2. A BSA will need an element to search.

"""


# This function returns an index of where that element is in the list.
def binary_search(a_list, number):

    # determine search space

    left = 0
    right = len(a_list) - 1

    # till search space consists of at-least one element
    while left <= right:

        # Search the mid point to compare with key value.

        mid = (left + right) // 2

        # key value is found, return an index
        if number == a_list[mid]:
            return mid

        # discard all elements in the right search space
        # including the mid element
        if number < a_list[mid]:
            right = mid - 1

        # discard all elements in the left search space
        # including the mid element
        else:
            left = mid + 1

    # search not found
    return None


if __name__ == '__main__':

    sorted_list = [1, 3, 5, 7, 9, 12]

    print(sum_all(sorted_list))

    if binary_search(sorted_list, 7) is not None:

        print("The number is founded.")

    else:

        print("The number is not founded")

