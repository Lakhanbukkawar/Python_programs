num=int(input("enter the n digit number"))
rev=0
orgnum=num
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if rev==orgnum:
    print('number is palindrome')
else:
    print('number is not palindrome')
              
              
