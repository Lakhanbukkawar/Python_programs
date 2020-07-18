x=[[12,15,88],
   [58,56,87],
   [77,13,17]]
for i in range(len(x)):
    for j in range(len(x[i])):
        if i!=j:
            x[i][j]=0
for r in x:
    print(r)
            
