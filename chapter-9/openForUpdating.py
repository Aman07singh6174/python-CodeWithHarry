st="\nRam is a good boy\n"
f=open("file2.txt","a+")# + = Open For Updating
f.write(st)
f.seek(0)
print(f.read())
f.close()