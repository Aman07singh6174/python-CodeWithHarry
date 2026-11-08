'''
1= snake
-1=water
0=gun

'''
import random
computer=random.choice([1,-1,0])
You=input("Choes the value \'snake' , \'water' or \'gun' :")
reversedValue={"snake":1,"water":-1,"gun":0}
value={1:"snake",-1:"water",0:"gun"}
if You not in reversedValue:
    print("Invalid Input! Better luck next time 😊")
else:
    you=reversedValue[You]
    print(f"Computer chose\t:{value[computer]}:\nYour input\t:{value[you]}")
    if(computer ==you):
        print("It's draw ! \n :Try agen:")
    else:
        if(computer==1 and you ==0 ):
            print("You Win!")
        elif(computer ==1 and you==-1):
            print("You lose!")
        elif(computer ==0 and you==1):
            print("You lose!")
        elif(computer ==0 and you ==-1):
            print("You Win!")
        elif(computer==-1 and you==0):
            print("You lose!")
        elif(computer==-1 and you ==1):
            print("You win!")

        