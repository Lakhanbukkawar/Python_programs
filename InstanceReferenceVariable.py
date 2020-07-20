class one():
    a:int
    b:int
    def __init__(self,x,y):
        self.a=x
        self.b=y
        print("constructer is called")
    def dis(self):
        print("a=",self.a)
        print("b=",self.b)


ob1=one(5,7)
ob1.dis()
ob2=one(9,11)
ob2.dis()
