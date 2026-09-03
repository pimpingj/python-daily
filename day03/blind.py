def longest_word(text):
    wnum = 0
    longestw = ""
    s = text.split()
    for sw in s:
        if len(sw) > wnum:
            wnum = len(sw)
            longestw = sw
    return longestw

t1 = "I love python"
t2 = "i wanna eat apples"
t3 = ""
t4 = "hola dos"

print(longest_word(t1))
print(longest_word(t2))
print(longest_word(t3))
print(longest_word(t4))
