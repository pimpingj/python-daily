def convert(text):
    text_con = text.split(",")
    return '-'.join(text_con)
    


c1="a,b,c"
c2="x,y,z,w"

print(convert(c1))
print(convert(c2))