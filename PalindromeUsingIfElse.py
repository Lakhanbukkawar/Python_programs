num=int(input('enter the three digit number'))
orgnum=num
n1=num%10
num=num//10
n2=num%10
num=num//10
rev=(n1*100)+(n2*10)+(num*1)
if rev==orgnum:
    print('the number is palindrome')
else:
    print('number is not palindrome')
