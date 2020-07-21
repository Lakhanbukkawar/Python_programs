a=int(input("enter the first number in arithematic series"))
d=int(input("enter the common difference of series"))
n=int(input("enter the number of terms"))
if(n>0):
    N=a+(n-1)*d
    print(N)
s=(n*(2*a+(n-1)*d))/2
print(s)
