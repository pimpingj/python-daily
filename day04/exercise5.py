def reverse_list(lst):
    result = []
    for x in range(len(lst) -1,-1,-1):
        result.append(lst[x])
    return result
        






r1 = [1, 2, 3]
r2 = ['a', 'b']
r3 = [1]
r4 = []

print(reverse_list(r1))
print(reverse_list(r2))
print(reverse_list(r3))
print(reverse_list(r4))