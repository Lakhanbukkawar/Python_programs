class one():
    a:int
    b:int
    def set1(self,v1,v2):
        self.a=v1
        self.b=v2

    def dis(self):
        print("a=",self.a)
        print("b=",self.b)

    def add(self,obj):
        print(self.a+obj.a)
        print(self.b+obj.b)

ob1=one()
ob1.set1(5,7)
ob1.dis()
ob2=one()
ob2.set1(6,8)
ob2.dis()
ob1.add(ob2)
