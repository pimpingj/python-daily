def group_by_length(words):
    result = {}
    for word in words:
        num = len(word)
        if num in result:
            result[num].append(word)
        else:
            result[num] = [word]
    return result

l1 = ["cat", "dog", "bird", "elephant", "monkey", "kangaroo", "crocodile"]
l2 = []

print(group_by_length(l1))
print(group_by_length(l2))
