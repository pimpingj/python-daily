def sort_by_length(words, reverse=False):
    return sorted(words, key=len, reverse=reverse)
        



s1 = ["banana", "kiwi", "apple"]
s2 = ["kiwi", "pear", "plum"]
print(sort_by_length(s1))
print(sort_by_length(s1, True))
print(sort_by_length(s2))
print(sort_by_length(s2, True))
print(sort_by_length([]))