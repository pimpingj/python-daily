def dedupe(lst):
    result = []
    seen = set() 
    for x in lst:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result



d1 = [1, 2, 2, 3, 1]
d2 = ['a', 'b', 'a', 'c']
d3 = []


print(dedupe(d1))
print(dedupe(d2))
print(dedupe(d3))