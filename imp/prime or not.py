num = int(input("Enter number to check prime or not:"))

if num <=1:
    print("Not Prime")
else:
    for i in range(2,num):
        if num % i == 0:
            print("not prime")
            break
        else:
            print("it Prime ")
            break