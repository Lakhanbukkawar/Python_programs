class one():
    a:int
    b:int
    def __init__(self):
        self.a=12
        self.b=13
        print("constructer is called")
    def dis(self):
        print("a=",self.a)
        print("b=",self.b)


ob1=one()
ob1.dis()
ob2=one()
ob2.dis()
