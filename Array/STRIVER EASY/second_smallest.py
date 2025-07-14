# if array is unique and sorted,and we wanna find second smallesr element then arr[1] is second smallest
# id array is unique and sorted,and we wanna find second largest element then arr[n-1] is second smallest

# Using python inbuilt functions

marks = [3,2,1,5,6,3,7]
sorted_array=sorted(marks)
print(f"Sorted Array is {sorted_array}")
unique_array = set(marks)
print(f"unique elements :{unique_array}")


final_list = list(unique_array)

print(f"Second Largest Element is : {final_list[len(final_list)-2]}")
print(f"Second Smallest Element is : {final_list[1]}")



# Using Two Pointers 

def second_smallest(arr):
    if arr[0]<arr[1]:
        smallest = arr[0]
        second_smallest =[1]
    else:
        smallest = arr[1]
        second_smallest = arr[0]

    for i in arr[2:]:
        if i<smallest:
            second_smallest = smallest
            smallest=1
        elif i<second_smallest and i!=smallest:
            second_smallest = i
        
    return second_smallest

arrey = [5,1,3,4,2]
second_smallest = second_smallest(arrey)

print(second_smallest)