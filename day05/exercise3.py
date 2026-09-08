def analyze(lst):
    if not lst:
        raise ValueError("the list is empty")
    largest = max(lst)
    smallest = min(lst)
    avg = sum(lst) / len(lst)
    return largest, smallest, avg

l1 = [4,2,56,7]
l2 = [66, 3, 23,57, 0]
l3 = []

largest, smallest, avg = analyze(l1)
print(largest, smallest, avg)
largest, smallest, avg = analyze(l2)
print(largest, smallest, avg)
largest, smallest, avg = analyze(l3)
print(largest, smallest, avg)