def analyze(lst):
    if not lst:
        raise ValueError("analyze()不接受空列表")
    largest = max(lst)
    smallest = min(lst)
    avg = sum(lst) / len(lst)
    
    return largest, smallest, avg

l1 = [2, 4, 7, 12, 54, 0]
l2 = []

largest, smallest, avg = analyze(l1)
print(largest, smallest, avg)
largest, smallest, avg = analyze(l2)
print(largest, smallest, avg)