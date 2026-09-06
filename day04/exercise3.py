def merge_sort(lst1, lst2):
    newlst = lst1 + lst2
    result = sorted(newlst)
    return result


m1 = [3, 1]
m2 = [4, 2]

m3 = [5]
m4 = []

m5 = []
m6 = []

m7 = [3, 1]
m8 = [1, 2]

print(merge_sort(m1, m2))
print(merge_sort(m3, m4))
print(merge_sort(m5, m6))
print(merge_sort(m7, m8))