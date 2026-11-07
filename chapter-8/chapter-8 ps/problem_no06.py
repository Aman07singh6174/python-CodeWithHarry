def rem(l,word):
    n=[]
    for item in l:
       if not(item == word ):
         n.append(item.strip(word))
    return n
l=["karry","harry", "aman","riya","your"]
print(rem(l,"y")) 