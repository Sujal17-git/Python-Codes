# USING MIN 

arr = [4,32,5,6,2,9]
print(min(arr))

#USING POINTER 

def min_element(arr):
    n = len(arr)
    smallest = arr[0]

    for i in range(1,n):
        if arr[i]<smallest:
            smallest= arr[i]
    return smallest

array = [3,4,5,33,10]
smallest_num = min_element(array)

print(f"Smallest Element is :{smallest_num}")