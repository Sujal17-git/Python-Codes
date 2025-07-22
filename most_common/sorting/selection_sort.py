def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min = i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr



arr =[3,2,1,4,5,6]
print(selection_sort(arr))
