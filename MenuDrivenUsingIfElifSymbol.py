print('press + for addition')
print('press - for substraction')
print('press * for multiplication')
print('press / for division')
ch=input('enter the number')
if ch=='+':
    num1=int(input('enter first number for addition'))
    num2=int(input('enter second number for addition'))
    res=num1+num2
    print('the addition is',res)
elif ch=='-':
    num1=int(input('enter first number for substraction'))
    num2=int(input('enter second number for substraction'))
    res=num1-num2
    print('the substraction is',res)
elif ch=='*':
    num1=int(input('enter first number for multiplication'))
    num2=int(input('enter second number for multiplication'))
    res=num1*num2
    print('the multiplication is',res)
elif ch=='/':
    num1=int(input('enter first number for division'))
    num2=int(input('enter second number for division'))
    res=num1/num2
    print('the division is',res)
else:
    print('invalid choice')
    
