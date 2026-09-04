def check_email(text):
    if "@" in text:
        email = text.split("@")
        if "." in email[1]:
            return True
        else:
            return False
    else:
        return False

c1 = "abc@gmail.com"
c2 = "abcgmail.com"
c3 = "abc@gmailcom"
c4 = "@gmail.com"
c5 = "a@b.c"

print(check_email(c1))
print(check_email(c2))
print(check_email(c3))
print(check_email(c4))
print(check_email(c5))