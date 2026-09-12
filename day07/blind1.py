def count_chars(text):
    result = {}
    for ch in text:
        result[ch] = result.get(ch, 0) + 1
    return result

s1 = "hello"
s2 = ""

print(count_chars(s1))
print(count_chars(s2))
