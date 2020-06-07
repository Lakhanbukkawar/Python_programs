print('press 1 for addition')
print('press 2 for substraction')
print('press 3 for multiplication')
print('press 4 for division')
ch=int(input('enter the number'))
if ch==1:
    num1=int(input('enter first number for addition'))
    num2=int(input('enter second number for addition'))
    res=num1+num2
    print('the addition is',res)
elif ch==2:
    num1=int(input('enter first number for substraction'))
    num2=int(input('enter second number for substraction'))
    res=num1-num2
    print('the substraction is',res)
elif ch==3:
    num1=int(input('enter first number for multiplication'))
    num2=int(input('enter second number for multiplication'))
    res=num1*num2
    print('the multiplication is',res)
elif ch==4:
    num1=int(input('enter first number for division'))
    num2=int(input('enter second number for division'))
    res=num1/num2
    print('the division is',res)
else:
    print('invalid choice')
    
