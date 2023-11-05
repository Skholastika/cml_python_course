from typing import List, Any


def max_len(list1: List[Any], list2: List[Any]):
    length1: int = len(list1)
    length2: int = len(list2)
    if length1 >= length2:
        return length1
    else:
        return length2


# a = ['sd', 'dfsfd0', 'sdf']
# b = [1, 2]
# c = ['werdo']
#
# print(max_len(a, b))
# print(max_len(b, c))
# print(max_len(c, a))
