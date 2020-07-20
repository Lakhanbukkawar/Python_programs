class Test:
    a=10
    def __init__(self):
        Test.b=20
    def m1(self):
        Test.c=30

ob1=Test()
print(ob1.a)
print(ob1.b)
print(ob1.c)
