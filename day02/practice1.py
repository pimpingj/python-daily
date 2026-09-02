def is_palindrome(text):
    return text == text[::-1]



t1="level"
t2="hello"
t3="abba"
t4=""

print(is_palindrome(t1))
print(is_palindrome(t2))
print(is_palindrome(t3))
print(is_palindrome(t4))