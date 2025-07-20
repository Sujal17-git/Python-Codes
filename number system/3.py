   

while True:
    n = int(input("Enter Number to check prime or not : "))
    prime=True

    for i in range(2,n):
        if n%i==0:
            prime = False

    if prime:
        print("Number Is Prime")
    else:
        print("Not Prime")
    
    if n != int:
        break