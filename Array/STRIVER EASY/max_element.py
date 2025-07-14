# Using Max

arr = [1,3,2,1,5,3,1]
print(max(arr))

# using brute force

def max_element(arr):
    n = len(arr)
    biggest = arr[0]

    for i in range(1,n):
        if arr[i]>biggest:
            biggest = arr[i]
    return biggest

my_list = [4,3,8,1,6,7]
max_element = max_element(my_list) 

print(max_element)


