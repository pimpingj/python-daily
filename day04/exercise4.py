def get_evens_loop(lst):
    result = []
    for x in lst:
        if x % 2 == 0:
            result.append(x)
    return result

def get_evens_comp(lst):
    return [x for x in lst if x % 2 == 0]
    

g1 = [1, 2, 3, 4, 5, 6]
g2 = [1, 3, 5]
g3 = []
g4 = [-2, -1, 0, 1]

print(get_evens_loop(g1))
print(get_evens_comp(g1))
print(get_evens_loop(g2))
print(get_evens_comp(g2))
print(get_evens_loop(g3))
print(get_evens_comp(g3))
print(get_evens_loop(g4))
print(get_evens_comp(g4))