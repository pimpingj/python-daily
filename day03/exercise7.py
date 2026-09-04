def chunk(text):
    chunks = []
    for i in range(0,len(text),3):
        chunks.append (text[i:i+3])
    return chunks

c1 = "abcdefghi"
c2 = "abcdefgh"
c3 = "ab"
c4 = ""

print(chunk(c1))
print(chunk(c2))
print(chunk(c3))
print(chunk(c4))