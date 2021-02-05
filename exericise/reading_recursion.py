def mystery_one(x, y):

    if y <= 0:
        return x

    elif y > 10:
        y = y//2
        return mystery_one(x, y)

    else:
        x = x + 1
        return mystery_one(x, y - 1)


# print(mystery_one(10, 1))
# print(mystery_one(10, 10))
# print(mystery_one(10, 20))
# print(mystery_one(5, -1))

def mystery_two(x):

    y = x // 2
    x = y - 1

    if x > 0:
        print("Recursion is running")
        y = y + mystery_two(x)

    return y


# print(mystery_two(10))
# print(mystery_two(20))

"""

Solving Method

mystery_two(10) --> return 7

y = 5
x = 4

mystery_two(4) --> return 2

y = 2
x = 1

mystery_two(1) --> return 0

y = 0
x = -1

"""


def mystery_three(x):
    y = x % 2
    x = x // 2
    if x > 0:
        y = y + mystery_three(x)
    return y


def iteratively_sum(a_list):

    number = 0

    for i in range(0, len(a_list)):
        number += a_list[i]

    return number


def iteratively_replace_to_none(a_list):

    for i in range(0, len(a_list)):

        if a_list[i] > 10:

            a_list[i] = None


def recursively_replace_to_none(a_list, start):

    if start == len(a_list):

        return

    else:

        if a_list[start] < 10:

            a_list[start] = None

        recursively_replace_to_none(a_list, start + 1)


def mystery(x):
    y = x % 2
    x = x // 2
    print("Compute " + str(x) + " and " + "Compute " + str(y))
    if x > 0:
        y = y + mystery(x)
    return y


def enigma(x):

    y = mystery(x)
    print("Engima y is " + str(y))

    if y > 1:
        y = y + enigma(y)
    return y


print(mystery(10))
