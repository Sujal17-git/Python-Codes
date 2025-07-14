age=int(input("Enter your age :"))

if(age>=18 and age<100):
    print("Eligable")
elif(age>0 and age<18):
    print("You are minor")
else:
    print("Enter valid age")
