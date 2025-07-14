def sorted_or_not(arr):
    
    result = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            result = False
    
    if result==True:
            print("Array is Sorted")
    else:
            print("Not Sorted ")
    


    

arr = [1,2,3,4,5]
sorted_or_not(arr)
