def parttern(n):
    if n==0:
        print("Inveled input!\n plese try next time!")
        return
    else:
        print("*"*n)
        parttern(n-1)
n=int(input("Enter the number to print the parttern :"))
parttern(n)