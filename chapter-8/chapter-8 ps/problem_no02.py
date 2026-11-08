def f_to_c(f):
    c=5*(f-32)/9
    return c
f=int(input ("Enter the f° value : "))
print (f"C° value of {f}F°:{round(f_to_c(f),2)}C°")