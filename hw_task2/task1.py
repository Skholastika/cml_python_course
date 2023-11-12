from typing import List


def del_stop_w(str0: str, stop_words: List[str] = ['Python', 'php', 'go', 'C']):
    words: List[str] = str0.split(' ')
    for word in stop_words:
        while word in words:
            words.remove(word)
    result: str = ' '.join(words)
    return result

# str0 = 'Mama loves Python Papa Python loves php php php Sister loves go And I php love C'
# print(str0)
# print(del_stop_w(str0))
# print(del_stop_w(str0, ['Mama', 'Papa', 'Sister']))
