def fibonacci_series(n, a=0, b=1):
    if n==0:
        return
    print(a, end=" ")
    fibonacci_series(n - 1, b, a + b)

fibonacci_series(10)


# Without Recursion

def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
