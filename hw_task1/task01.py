def str_len_v1(string: str):
    length: int = len(string)
    return length

def str_len_v2(string):
    length: int = 0
    for simbol in string:
        length += 1
    return length

# print(str_len_v1(""))
# print(str_len_v2(""))
# print(str_len_v1("kjh3"))
# print(str_len_v2("kje3"))
