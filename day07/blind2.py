def merge(base, override):
    result = {}
    for k, v in base.items():
        result[k] = v
    for k, v in override.items():
        result[k] = v
    return result

l1 = {'a' : 1, 'b' : 2, 'c' : 3}
l2 = {'a' : 2, 'c' : 3, 'd' : 4}
l3 = {}

print(merge(l1, l2))
print(merge(l1, l3))