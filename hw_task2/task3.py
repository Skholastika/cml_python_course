from typing import List, Any


def only_str(*args: Any):
    strs: List[str] = []
    for item in args:
        if type(item) is str:
            strs.append(item)
    return tuple(strs)


# print(only_str(1, '3', ['asd', 'sda', 'sdsa'], 323.11, '877.323', (2, '02'), {'ss': 1, 5: '3'}))
# print(only_str('one', 'two', 3, 4.0))
