num=int(input('enter any three digit number'))
n1=num%10
num=num//10
n2=num%10
num=num//10
n3=num%10
rev=(n1*100)+(n2*10)+(n3*1)
print(rev)
