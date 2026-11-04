student_marks=[]

M1=int(input("Enter the 01 student marks: "))
student_marks.append(M1)

M2=int(input("Enter the 02 student marks:"))
student_marks.append(M2)

M3=int(input("Enter the 03 student marks:"))
student_marks.append(M3)

M4=int(input("Enter the 04 student marks:"))
student_marks.append(M4)    

M5=int(input("Enter the 05 student marks:"))    
student_marks.append(M5)

M6=int(input("Enter the 06 student marks:"))
student_marks.append(M6)

M7=int(input("Enter the 07 student marks:"))
student_marks.append(M7)

student_marks.sort()#sort the list in ascending order

print(student_marks)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

tuple=(1, 2, 3, 4, 5.2, "hello", True)

# tuple[1]=10#this will give an error because tuples are immutable data types in python. once a tuple is created, it cannot be modified. Tuples are defined using parentheses () and can contain elements of different data types.

#===================================================================================================================================================================================================================================================

t=(1,2,3,4,5,6,7,8,9,10)
print(sum(t))