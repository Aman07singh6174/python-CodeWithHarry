def sum_rec(number):
    if(number == 1):
     return 1
    
    number=sum_rec(number-1)+number
    return number
number=int(input("Enter the number of geting rec value : "))
print(sum_rec(number))