n = 6

for i in range(1,6):
    for j in range(n-i):
        print(" ",end="")
    for k in range((2*i)-1):
        print(k+1,end="")

    print()