a=(1, 2, 3,2, 4, 5.2, "hello", True)

no=a.count(1)#count the number of occurrences of 1 in the tuple
print(no)

ns=a.index(2)#return the index of the first occurrence of 2 in the tuple     
print(ns)

print(len(a))#return the length of the tuple

#unpacking of tuples    
s,d,f,g,h,c,v,b=a#unpacking of tuples
print(s,d,f,g,h,c,v,b)
