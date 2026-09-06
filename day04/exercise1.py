import math

def find_max(lst):
    maxnum = -math.inf
    if not lst:
        raise ValueError("The input is empty")
    for num in lst:
        if num > maxnum:
            maxnum = num
        
    return maxnum

f1 = [3, 7, 2, 9, 1]
f2 = [5]
f3 = [-3, -7, -1]
f4 = []

print(find_max(f1))
print(find_max(f2))
print(find_max(f3))
print(find_max(f4))