def factorial(n,ans=1):
    if n>1:
        ans*=n
        factorial(n-1,ans)
    else:
        print(f"Factorial is {ans}")

factorial(10)