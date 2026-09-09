def count_chars(text):
    dic = {}
    for ch in text:
        dic[ch] = dic.get(ch,0) + 1
    return dic


t1 = "Hello"
t2 = "I Love python"
t3 = "i'm 12 years old"
t4 = ""

print(count_chars(t1))
print(count_chars(t2))
print(count_chars(t3))
print(count_chars(t4))