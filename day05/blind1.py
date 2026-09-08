def dedupe(lst):
    result = []
    seen = set()
    for x in lst:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result

l1 = [1,2,3,1,3,2]
l2 = [3,6,4,7,3,4,5,6]

print(dedupe(l1))
print(dedupe(l2))