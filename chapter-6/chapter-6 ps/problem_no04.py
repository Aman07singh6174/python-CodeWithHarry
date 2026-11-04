UserName=input("Enter your name: ")
if (len(UserName)<10):
    print("Your name is too short")
elif (len(UserName)>30):
    print("Your name is too long")
else:
    print(UserName)