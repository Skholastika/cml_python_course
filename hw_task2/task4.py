from typing import List, Any


def comparing(list1: List[Any], list2: [Any]):
    result: List[Any] = []
    for item in list1:
        if item in list2 and type(item) is not bool:
            result.append(item)
    return result


# print(comparing([1, 'list', 5.0, [5, 6, 7], 10.0], [1, 5.0, 5, [5, 6, 7, 8], 10.0]))
# print(comparing([1, 'list', 5.0, True, [5, 6, 7], 10.0], [1, 5.0, 5, [5, 6, 7, 8], 10.0]))
# print(comparing([1, 'list', 5.0, True, [5, 6, 7], 10.0], [1, 5, 5.0, [5, 6, 7, 8], 10.0]))
