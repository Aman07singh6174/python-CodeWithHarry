a1=int(input("Enter the first number: "))
a2=int(input("Enter the second number: "))
a3=int(input("Enter the third number: "))
a4=int(input("Enter the fourth number: "))
if a1>a2 and a1>a3 and a1>a4:
    print("The first number is the greatest.")
elif a2>a1 and a2>a3 and a2>a4:
    print("The second number is the greatest.")
elif a3>a1 and a3>a2 and a3>a4:
    print("The third number is the greatest.")
else:
    print("The fourth number is the greatest.")
    