n = 5

for i in range(n):
    for j in range(5,i,-1):
        print(j,end=" ")
    print()

for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(n-i,0,-1):
        print(k,end=" ")
    print()