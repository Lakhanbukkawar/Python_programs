def add():
    """Addition Program"""
    print(add.__doc__)
    num1=int(input("enter first number: "))
    num2=int(input("enter second number: "))
    res=num1+num2
    print("additon=",res)
def sub():
    """Substraction Program"""
    print(sub.__doc__)
    num1=int(input("enter first number: "))
    num2=int(input("enter second number: "))
    res=num1-num2
    print("substraction=",res)
def mul():
    """Multiplication Program"""
    print(mul.__doc__)
    num1=int(input("enter first number: "))
    num2=int(input("enter second number: "))
    res=num1*num2
    print("multiplication=",res)
def div():
    """Division program"""
    print(div.__doc__)
    num1=int(input("enter first number: "))
    num2=int(input("enter second number: "))
    res=num1//num2
    print("division=",res)
print("press 1 for addition")
print("press 2 for substraction")
print("press 3 for multiplication")
print("press 4 for division")
ch=int(input("enter your choice"))
x=1
while(x==1):
 if ch==1:
    add()
 elif ch==2:
    sub()
 elif ch==3:
    mul()
 elif ch==4:
    div()
 #elif
  #  print("invalid choice")
 else:
  break
