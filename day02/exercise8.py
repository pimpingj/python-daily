def longest_word(text):
    maxnum = 0
    maxtext = ""
    text_con = text.split()
    for texts in text_con:
        if len(texts) > maxnum:
            maxnum = len(texts)
            maxtext = texts
    return maxtext



l1="I love python programming"
l2="a bb ccc"
l3="cat dog"
l4=""

print(longest_word(l1))
print(longest_word(l2))
print(longest_word(l3))
print(longest_word(l4))