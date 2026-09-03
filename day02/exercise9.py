def fix_python(text):
    s = text.replace("python", "Python")
    return s

f1 = "Python and python"
print(fix_python(f1))