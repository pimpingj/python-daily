def string_info(s):
    num = len(s)
    cap = s.upper()
    rev = s[::-1]
    return num, cap, rev

s1 = "Hello"
s2 = "Dechland"
s3 = ""
num, cap, rev = string_info(s1)
print (num, cap, rev)
num, cap, rev = string_info(s2)
print (num, cap, rev)
num, cap, rev = string_info(s3)
print (num, cap, rev)
