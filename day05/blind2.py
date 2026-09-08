def second_largest(lst):
    lstun = sorted(set(lst), reverse=True)
    if len(lstun) <= 1:
        raise ValueError("second_largest() 需要至少两个不同的数值")
    return lstun[1]


l1 = [4,2,5,1,2,5,7]

print(second_largest(l1))

