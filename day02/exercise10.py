def count_words(text):
    s = text.split()
    return len(s)

c1= "I love python"
c2= "hello"
c3= ""
c4= "  a   b  "

print(count_words(c1))
print(count_words(c2))
print(count_words(c3))
print(count_words(c4))
