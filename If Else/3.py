#find largest number in 3 number 
num1 = int(input("Enter First number :"))
num2 = int(input("Enter Second number :"))
num3 = int(input("Enter third number :"))

if(num1>num2):
    if(num1>num3):
        print("Number 1",num1,"is biggest")
    else:
        print("Number 3",num3,"is biggest")
else:
    if(num2>num3):
        print("Number 2 is",num2," biggest")
    else:
        print("Number 3",num3,"is biggest")