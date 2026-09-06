#统计一段英文里每个字母出现的次数，返回字典，忽略大小写，跳过非字母
def count_letters(text):
    letters = {}
    word = text.lower()
    for ch in word:
        if ch.isalpha():
            if ch in letters:
                letters[ch] += 1
            else:
                letters[ch] = 1
    return letters

t1 = "i love you"
t2 = " How are you?"
t3 = ""
t4 = "i have left 3 days"

print(count_letters(t1))
print(count_letters(t2))
print(count_letters(t3))
print(count_letters(t4))