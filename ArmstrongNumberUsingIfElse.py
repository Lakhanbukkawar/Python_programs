num=int(input('enter any three digit number '))
orgnum=num
n1=num%10
num=num//10
n2=num%10
num=num//10
res=(n1**3)+(n2**3)+(num**3)
if res==orgnum:
    print('entered number is armstrong')
else:
    print('entered number is not armstrong')
