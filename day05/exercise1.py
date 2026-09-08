a1 = [1, 2]
b1 = a1[:]
b1.append(3)
print("切片:", a1, b1)

a2 = [1, 2]
b2 = list(a2)
b2.append(3)
print("list():", a2, b2)

a3 = [1, 2]
b3 = a3.copy()
b3.append(3)
print(".copy():", a3, b3)