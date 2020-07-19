#def add(*num):
 #   sum=0
#for n in num:
 #   sum=sum+n
#print("Sum: ",sum)
#add(3,5)
#add(25,35,55)

def adder(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)
