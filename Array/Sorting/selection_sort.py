def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index=i

        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index = j
        
        arr[i],arr[min_index] = arr[min_index],arr[i]

    return arr
    
my_list = [3,5,2,1,6,9]

sorted_array = selection_sort(my_list)

print(f"Sorted Array : {sorted_array}")