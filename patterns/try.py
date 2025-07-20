for i in range(5):
    for j in range(i):
        print(" ",end="")
    for k in range(5-i):
        print("*",end=" ")
    print()

for i in range(4):
    for j in range(4-i-1):
        print(" ",end="")
    for k in range(i+2):
        print("*",end=" ")
    print()
