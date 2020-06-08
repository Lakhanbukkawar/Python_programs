num=int(input('enter the n digit number'))
num1=num
add=0
for val in range(num1,0,-1):
    r=num1%10
    add=add+r**3
    num1=num1//10
if num==sum:
    print('number is armstrong')
else:
    print('number is not armstrong')
