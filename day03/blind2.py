def count_words(text):
    s = text.split()
    return len(s)

t1 = "i am a student"
t2 = "guten Tag!"
t3 = ""

print(count_words(t1))
print(count_words(t2))
print(count_words(t3))