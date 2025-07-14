def sum_of_n(n):
    if n == 0:
        return 0
    return n + sum_of_n(n - 1)

# Example
result = sum_of_n(5)
print("Sum:", result)

# Using Functional Arguments

def sum_of_n(n, sum=0):
    if n > 0:
        sum += n
        sum_of_n(n - 1, sum)
    else:
        print("Sum:", sum)

sum_of_n(5)
