a=int(input("What is your age? "))
#indipendent  if statement
if a%2==0:
    print("Your age is even.")

    #end of if statement

 #indipendent  elif statement   
if a>=18:
    print("You are eligible to vote.")  
elif a<=0:
    print("invalid age. Please enter a valid age.")
else:
    print("You are not eligible to vote.")
    #end of elif statement