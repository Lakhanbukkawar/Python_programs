mat1=[[5,0,0],[0,8,0],[0,0,6]]
count=0
for x in range(0,3):
    for y in range(0,3):
        if(x!=y and mat1[x][y]==0):
            count=count+1
if(count==6):
    print("it's a diagonal matrix")
else:
    print("it's not a diagonal matrix")
