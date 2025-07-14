def found_or_not(arr,n):
    length = len(arr)
    found = False

    for i in range(length):
        if arr[i] == n:
            print(f"Value Found on {i} index")
            found = True
    if found==False:
        print("Element Not Found")
        
arr = [1,2,3,4,5,1]
found_or_not(arr,8)
