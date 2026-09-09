def reverse_list(lst):
    result = []
    for i in range(len(lst) -1, -1, -1):
        result.append(lst[i])
    return result

l1 = [1, 2, 3, 4, 5, 6]
l2 = []
l3 = ['a', 'b', 'c']


print(reverse_list(l1))
print(reverse_list(l2))
print(reverse_list(l3))