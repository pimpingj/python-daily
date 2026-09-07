def second_largest(lst):
    lstun = sorted(set(lst),reverse=True)
    if len(lstun) <= 1:
        raise ValueError("second_largest() 不接受单元素以及空列表")
    return lstun[1]


s1 = [3, 7, 2, 9, 1]
s2 = [5, 5, 3]
s3 = [4, 4]
s4 = [5]

print(second_largest(s1))
print(second_largest(s2))
print(second_largest(s3))
print(second_largest(s4))