n = 5

for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(n,i,-1):
        print("*",end=" ")
    print()