def even_odd(a):
    if a%2==0:
        return "it is even"
    return "it is odd"
num=int(input("enter a number to check if it is even or odd\n"))
print(num)
print(even_odd(num))
