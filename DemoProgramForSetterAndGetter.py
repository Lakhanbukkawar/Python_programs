class student:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def setMarks(self,marks):
        self.marks=marks

    def getMarks(self):
        return self.marks

n=int(input("enter number of students: "))
for i in range(n):
    s=student()
    name=input('enter name: ')
    s.setName(name)
    marks=int(input("enter marks: "))
    s.setMarks(marks)

    print('Hi',s.getName())
    print("your marks are: ",s.getMarks())
    print()
