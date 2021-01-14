some_list = [9,8,7,6,5,4,3,2,1]


def find_intervals(a_list):

    separators = [0]

    for i in range(0, len(a_list), 1):

        if i == len(a_list)-1:
            separators.append(len(a_list))
            break

        if some_list[i] < some_list[i + 1]:
            pass
        elif some_list[i] > some_list[i + 1]:
            separators.append(i + 1)


    return separators


print(find_intervals(some_list))