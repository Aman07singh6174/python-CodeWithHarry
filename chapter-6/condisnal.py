a=int(input("What is your age? "))

if a>=18:
    print("You are eligible to vote.")  
elif a<=0:
    print("invalid age. Please enter a valid age.")
else:
    print("You are not eligible to vote.")