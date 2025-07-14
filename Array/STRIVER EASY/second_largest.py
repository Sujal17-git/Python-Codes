def second_largest(arr):
    if arr[0]<arr[1]:
        largest = arr[1]
        second_largest = arr[0]
    else:
        second_largest=arr[1]
        largest= arr[0]
    n = len(arr)

    for i in arr[2:]:
        if i>largest:
            second_largest = largest
            largest = i
        elif i>second_largest and i!=largest:
            second_largest = i

    return second_largest

arr=[2,4,1,6,7,5,9,15]
second_largest_ele = second_largest(arr)
print(f"Second Largest element is {second_largest_ele}")
            