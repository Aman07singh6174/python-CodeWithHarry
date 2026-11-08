def max(n1,n2,n3):
    if(n1>n1 and n1>n3):
        return (f"{n1} is the max of  {n2,n3}")
    elif(n2>n1 and n2>n3):
        return(f"{n2} is the max of {n1,n3}")
    elif(n3>n2 and n3>n1):
        return(f"{n3} is the max of  {n1,n2}")
n1=int(input("Enter the number to find max n1 :"))
n2=int(input("Enter the number to find max n2 :"))
n3=int(input("Enter the number to find max n3 :"))

print(max(n1,n2,n3))