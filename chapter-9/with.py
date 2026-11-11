f=open("file.txt")
print(f.read())
f.close

#=================================#
# using with no need to close
# ================================#

with open ("file.txt")as f:
    print(f.read())
