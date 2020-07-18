from array import *
a=array('i',[])
for x in range(0,5):
    s=int(input('enter the array elements'))
    a.append(s)
sum=0
for q in range(0,5):
    sum=sum+a[q]
print(sum)
    
