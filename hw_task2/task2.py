from typing import List


def multiples(a: int, list0: List[int] = range(1, 31)):
    result: List[int] = []
    for item in list0:
        if item % a == 0:
            result.append(item)
    return result


# print(multiples(5))
# print(multiples(5, [0, 5, 10, 44, 232, 22, 55, 45]))
