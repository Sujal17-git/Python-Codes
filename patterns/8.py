for i in range(5):
    for j in range(i):
        print(" ",end="")
    for k in range(2*(5-i)-1):
        print("*",end="")
    print()