n=6 

for i in range(1,n):
    for j in range(1,n):
        print(j,end=" ")
    print()

print()

for i in range(1,n):
    for j in range(i):
        print((j+1)*2,end=" ")
    print()