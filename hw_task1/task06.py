from typing import List, Union


def positive_count(list0: List[Union[int, float]]):
    counter: int = 0
    for elem in list0:
        if elem > 0:
            counter += 1
    return counter


#print(positive_count([0, 10, 656.55, -654, -65.5, -0, 0.0]))
