#写一个函数，统计一段英文里每个字母出现的次数
def count_letters(text):
    times={}
    s = text.lower()
    for ch in s:
        if ch.isalpha():
            if ch in times:
                times[ch] = times[ch] + 1
            else:
                times[ch] = 1
    return times

    


c1 ="hello"
c2 = "banana"
c3 = "abandon"
c4 = "Hello World"
print(count_letters(c1))
print(count_letters(c2))
print(count_letters(c3))
print(count_letters(c4))