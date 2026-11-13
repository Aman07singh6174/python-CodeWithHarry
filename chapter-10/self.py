class employee: #class attribut
    lang="py"
    salary=900

    def getInfo(self):
        print(f"lang:{self.lang},salary:{self.salary}")

riya=employee()
riya.lang="js" #instence attribut
# print(riya.lang,riya.salary)
riya.getInfo()#both are same employee.getInfo(riya)

