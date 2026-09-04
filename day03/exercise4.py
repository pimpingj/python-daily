def to_snake(text):
    result = ""
    for ch in text:
        if ch.isupper():
            result += "_" + ch.lower()
        else:
            result += ch
    return result

t1 = "helloWorldFoo"
t2 = "userName"
t3 = "hello"

print(to_snake(t1))
print(to_snake(t2))
print(to_snake(t3))
