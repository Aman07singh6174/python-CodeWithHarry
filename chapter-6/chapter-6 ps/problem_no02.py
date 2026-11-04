mask1=int(input("Enter the first number: "))
mask2=int(input("Enter the second number: "))
mask3=int(input("Enter the third number: "))
mask4=int(input("Enter the fourth number: "))

total_percentage=(100*(mask1+mask2+mask3+mask4)/400)
s=(mask1 < 40 or mask2 < 40 or mask3 < 40 or mask4 < 40)
if (s):
     print("Your grade is F")

if (mask1 < 40):
        print("You failed in Subject 1")

if (mask2 < 40):
        print("You failed in Subject 2")

if (mask3 < 40):
        print("You failed in Subject 3")

if (mask4 < 40):
        print("You failed in Subject 4")

if (not s):        

    if (total_percentage>=90 ):
     print("Your grade is A+")
    elif (total_percentage>=80 ):
     print("Your grade is A")    
    elif (total_percentage>=70 ):
     print("Your grade is B")
    elif (total_percentage>=60 ):
     print("Your grade is C")    
    elif (total_percentage>=50 ):
     print("Your grade is D")    
    elif (total_percentage>=40 ):
     print("Your grade is E") 

 


print("Your total percentage is: ",total_percentage,"%")