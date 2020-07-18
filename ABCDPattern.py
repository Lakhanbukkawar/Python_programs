x=65
for i in range(0,6):
    ch=chr(x)
    x=x+1
    for j in range(0,i+1):
        print(ch,end=' ')
    print('\r')
    
