def sinewave(height,length):
    innerspace=1
    outerspace=2
    for i in range(1,height+1):
        for j in range(1,length+1):
            for s in range(1, outerspace+1):
                print(end=" ")
            print("*",end="" )
            for s in range(1, innerspace+1):
                print(end=" ")
            print("*",end="")
            for s in range(1, outerspace+1):
                print(end=" ")
            print(end=" ")
        if (i+1!=height):
            outerspace=1
        else:
            outerspace=0
        if(i+1!=height):
            innerspace=3
        else:
            innerspace=5
        print()

height,length=5,10          
sinewave(height,length)
