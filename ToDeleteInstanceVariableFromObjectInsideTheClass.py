class one():
    a:int
    b=0
    def __init__(self):
        self.a=12
        self.b=13
        del self.b
        print("constructor is called")
    def dis(self):
        print("a=",self.a)
        print("b=",self.b)

ob1=one()
ob1.dis()
