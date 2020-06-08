num=int(input('enter n didgit number'))
add=0
while num>0:
    n1=num%10
    add=add+n1
    num=num//10
print(add)
