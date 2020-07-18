from array import*
ar=array('i',[])
for i in range(0,5):
    s=int(input("enter array elements: "))
    ar.append(s)
for i in range(0,5):
    for j in range(i+1,5):
        if (ar[i]>ar[j]):
            temp=ar[j]
            ar[j]=ar[i]
            ar[i]=temp

print("sorted array elements are: ",ar)
