def invert(mapping):
    result = {}
    for k, v in mapping.items():
        result[v] = k
    return result

m1 = {'a' : 1, 'b' : 2, 'c' : 3}
m2 = {'a' : 1, 'b' : 1}
m3 = {'a' : [1, 2, 3],'b' : 2}

print(invert(m1))
print(invert(m2))
print(invert(m3))