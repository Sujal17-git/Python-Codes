def left_rotate(arr):
    n = int(input("For How Many Place You wanna left rotate arr: "))

    for i in range(n):
        item = arr.pop(0)
        arr.append(item)
    print(arr)

arr=[1,2,3,4,5,6,7]
left_rotate(arr)

