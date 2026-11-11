f=open("file.txt")
line=f.readlines()  #readlines
print(line,type(line))
f.close()

# =========================================#

f=open("file.txt")
line2=f.readline() #readline
print(line2,type(line2))
f.close()