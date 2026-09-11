def merge(base, override):
    result = {}
    for k, v in base.items():
        result[k] = v
    for k, v in override.items():
        result[k] = v
    return result

a = {"name": "George", "age": 22, "major": "Computer Science"}
b = {"city": "Northampton", "country": "UK", "hobby": "weight training"}
c = {"name": "George", "age": 22, "major": "Computer Science"}
d = {"name": "Alex", "city": "Northampton", "hobby": "weight training"}
e = {}
f = {}

print(merge(a, b))
print(merge(c, d))
print(merge(c, e))
print(merge(f, c))
print(merge(e, f))