x=[[2,3],
   [6,7]]
y=[[5,4],
   [1,9]]
result=[[x[i][j]-y[i][j] for j in range(len(x[0]))]for i in range(len(x))]
for r in result:
    print(r)
