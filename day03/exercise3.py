def is_number(num):
    return num.isdigit()

n1  = "12345"
n2 = "12a45"
n3 = ""
n4 = "-12"
n5 = "1.5"

print(is_number(n1))
print(is_number(n2))
print(is_number(n3))
print(is_number(n4))
print(is_number(n5))