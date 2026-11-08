# #     *
# #   * * *
# # * * * * *
for i in range(1,3+1):
    print(" "*(3-i),end=" ")
    print("*"*(2*i-1),end=" ")
    print()
# #===========================================================

# # *
# # **
# # ***
for i in range(1,3+1):
   
    print("*"*i,end=" ")
    print()

# #----------------------------------------------------------------------------

# #   *
# #  **
# # ***

for i in range(1,3+1):
    print(" "*(3-i),end=" ")
    print("*"*i,end=" ")
    print()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# * * * 
# *   *
# * * *

for i in range(1,4):
    if(i==1 or i==3): 
     print("* "*3)
    else:
       print("*",end="")
       print(" "*3,end="") 
       print("*",)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# * * * 
# *   *
# *   *
# * * *

n=int(input("Enter the number:"))
for i in range(1,n+1):
   if(i==1 or i==n):
      print("* "*n)
   else:
      print("*",end="")
      print(" "*(2*n-3), end="")
      print("*")

# ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
# *** 
# * *
# * *
# ***

n=int(input("Enter the number:"))
for i in range(1,n+1):
   if(i==1 or i==n):
      print("*"*n)
   else:
      print("*",end="")
      print(" "*(n-2), end="")
      print("*")
