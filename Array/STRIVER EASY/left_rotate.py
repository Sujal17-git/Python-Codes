def left_rotate(arr):
    counter = 0
    while counter<3:
        temp = arr[0]
        arr.pop(0)
        arr.append(temp)
        counter+=1
    return arr

arr = [4,3,2,5,1]
result = left_rotate(arr)

print(result)