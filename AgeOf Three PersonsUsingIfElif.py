p1=int(input('enter the age of first person'))
p2=int(input('enter the age of second person'))
p3=int(input('enter the age of third person'))
if p1>p2 and p1>p3:
    print('p1 is greater')
elif p2>p1 and p2>p3:
    print('p2 is greater')
else:
    print('p3 is greater')
