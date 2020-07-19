a=[]
n=int(input('enter the number of elemnts in list:'))
for x in range(0,n):
    ele=int(input("enter element" +str(x+1) + ";"))
    a.append(ele)
b=set()
unique=[]
for x in a:
    if x not in b:
        unique.append(x)
        b.add(x)
print("non-duplicate items:")
print(unique)
