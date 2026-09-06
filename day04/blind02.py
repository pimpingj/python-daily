#驼峰转下划线
def to_snake(text):
    result = []
    for ch in text:
        if ch.isupper():
            result.append("_" + ch.lower())
        else:
            result.append(ch)

    return ''.join(result)

t1 = "helloWorldFoo"
t2 = "hellopython"
t3 = "hello Honey"
t4 = ""

print(to_snake(t1))
print(to_snake(t2))
print(to_snake(t3))
print(to_snake(t4))