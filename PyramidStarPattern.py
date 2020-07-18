sp=1
star=1
for i in range(1,5):
    for sp in range(1,39-i,sp+1):
        print(" ")
    for star in range(1,i,star+1):
        print(end=" * ")
    print(" ")
