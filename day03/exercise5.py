def capitalize_words(text):
    n = text.split()
    x = [s.capitalize() for s in n]  
    return ' '.join(x)


t1 = "hello world"
t2 = "i love python"
t3 = "it's ok"

print(capitalize_words(t1))
print(capitalize_words(t2))
print(capitalize_words(t3))