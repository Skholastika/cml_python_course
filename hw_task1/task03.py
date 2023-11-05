from typing import List, Any


def list_append(list_before: List[Any], elem: Any):
    list_after: List[Any] = list_before + [elem]
    return list_after

# a = [1, 2, 3]
# b = 'elem'
# print(list_append(a, b))

