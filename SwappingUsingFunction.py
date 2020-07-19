def swap(a,b):
    temp=a
    a=b
    b=temp
    return(a,b)

num1=int(input('enter a number'))
num2=int(input('enter a number'))
print("swapped number is",swap(num1,num2))
