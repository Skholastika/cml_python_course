from typing import List
def abbreviation(string: str):
    try:
        words: List[str] = string.split()
        if len(words) < 2:
            raise Exception("Less than 2 words!")


        for k in range(len(words)):
            words[k] = words[k][0]

        abb = ''.join(words)
        print(abb.upper())

    except Exception as ex:
        print("Wrong data format!")


# abbreviation('comp mech lab')
# abbreviation('CompMechLab')
# abbreviation(['Comp', 'Mech','Lab'])