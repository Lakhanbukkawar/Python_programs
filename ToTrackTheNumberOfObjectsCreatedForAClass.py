class student:
    counter=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.counter +=1

    def printDetails(self):
        print(self.name,self.age,"years old")



student1=student('jay','21')
student2=student("ram","23")
student3=student("shiv","25")

print("total number of objects created: ",student.counter)
