def sort_by2(element):
    return element[1]


elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
print(f'Before: {elements}')
elements.sort()
print(f'After sorting by 1st element: {elements}')
elements.sort(key=sort_by2)
print(f'After sorting by 2nd element: {elements}')
