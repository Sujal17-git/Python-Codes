# factorial series

n = int(input("Enter number :"))


factorial =1
for i in range(1, n+1):
    factorial *=i
    print(f"Factorial of {i}: {factorial}")