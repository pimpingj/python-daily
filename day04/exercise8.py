def chunk_list(lst, size= 3):
   result = []
   for i in range(0,len(lst),size):
    result.append(lst[i:i+size]) 
   return result



c1 = [1,2,3,4,5,6,7]
c2 = [1,2]
c3 = []
c4 = [1,2,3,4,5]

print(chunk_list(c1))
print(chunk_list(c2))
print(chunk_list(c3))
print(chunk_list(c4, 2))