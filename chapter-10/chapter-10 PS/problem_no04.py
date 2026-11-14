from random import randint
class trine:
    def __init__(self):
     self.trineNumber=randint(2000,9999)

    def book(self,fro,to):
       print(f"tecet is book trineNumber is {self.trineNumber},from {fro} to {to}")

    def getstetus(self):
       print(f" trineNumber is {self.trineNumber} is at a time..!")

    def getfare(self,fro,to):
       print(f"tecet fare  as trineNumber {self.trineNumber},from {fro} to {to} is {randint(100,2000)}" )

t=trine()
t.book("delhi","jaunpur")
t.getstetus()
t.getfare("delhi","jaunpur")