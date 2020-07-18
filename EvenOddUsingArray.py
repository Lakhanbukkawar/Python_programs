from array import *
a=array('i',[])
for x in range(0,5):
    s=int(input('enter the array elemnts: '))
    a.append(s)
even=0
odd=0
for q in range(0,5):
    if a[q]%2==0:
        even=even+a[q]
    else:
        odd=odd+a[q]
print(even)
print(odd)
              
