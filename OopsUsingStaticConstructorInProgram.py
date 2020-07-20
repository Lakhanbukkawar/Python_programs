class one:
    a=10

    def __init__(self):
        self.y=20


ob1=one()
ob2=one()
ob3=one()
ob1.y=12
print("ob1 a=",ob1.a," b= ",ob1.y)
ob2.y=13
print("ob2 a=",ob2.a," b =",ob2.y)
ob3.y=15
print("ob3 a=",ob3.a," b=",ob3.y)
one.a=14
print("ob1 a=",ob1.a," b=",ob1.y)
print("ob2 a=",ob2.a," b=",ob2.y)
print("ob3 a=",ob3.a," b=",ob3.y)
