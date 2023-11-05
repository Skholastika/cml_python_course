lst = [2, 4, 5, 8, 9, 13]

# for number in range(len(lst)):
#     lst[number] *= number
#     print(lst)

n = 0
while n < len(lst):
    lst[n] *= n
    print(lst)
    n += 1
