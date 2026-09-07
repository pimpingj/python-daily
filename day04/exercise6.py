def stats(lst):
    
    if not lst:
        raise ValueError("stats() 不接受空列表")
    total = sum(lst)
    return total, total/len(lst)


s1 = [1, 2, 3, 4]
s2 = [5]
s3 = []


print(stats(s1))
print(stats(s2))
print(stats(s3))