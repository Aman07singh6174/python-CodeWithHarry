def rec(number):
    if (number==1 or number==0):
        return 1
    else:
        return number*(rec(number-1))#that a fotmula and rec are call after complited the string
    
number=int(input("Enter the number : "))
print(f"Fect of {number} : ",rec(number))