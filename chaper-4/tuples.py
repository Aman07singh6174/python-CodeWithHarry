# tuples are immutable data types in python. once a tuple is created, it cannot be modified. Tuples are defined using parentheses () and can contain elements of different data types.
a=(1, 2, 3, 4, 5.2, "hello", True)
print(a)
print(type(a))#<class 'tuple'>

b=()#empty tuple
print(b)
print(type(b))#<class 'tuple'>

c=(1)
print(c)
print(type(c))#<class 'int'> because it is not a tuple, it is an integer

d=(1,)#single element tuple
print(d)
print(type(d))#<class 'tuple'>