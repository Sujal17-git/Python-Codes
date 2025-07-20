def check_sorted(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            sorted = False
    if sorted:
        print("Array is Sorted")
    else:
        print("Not Sorted")

def left_rotate(arr):
    copy = arr[:]
    item = copy.pop(0)
    copy.append(item)
    print(copy)

def right_rotate(arr):
    copy = arr[:]
    item = copy.pop(-1)
    copy.insert(0,item)
    print(copy)
    


arr =[1,2,3,7,8,9]
check_sorted(arr)
left_rotate(arr)
right_rotate(arr)
