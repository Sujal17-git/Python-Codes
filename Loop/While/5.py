#find total digit of intiger

n = int(input("Enter any number : "))

count = 0

if(n == 0):
    count =1
else:
    n = abs(n)
    while (n>0):
        n = n//10
        count +=1

print("Number digit is :",count)
