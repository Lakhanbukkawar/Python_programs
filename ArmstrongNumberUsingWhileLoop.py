num=int(input("enter the n digit number"))
add=0
temp=num
while temp>0:
    digit=temp%10
    add+=digit**3
    temp//=10
if num==add:
    print('the number is armstrong')
else:
    print("the number is not armstrong")
