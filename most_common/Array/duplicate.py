def duplicate(arr):
    new =[]
    for index,value in enumerate(arr):
        if value not in new:
            new.append(value)
        else:
            print(f"Repeated value:{value}")


arr=[1,2,3,4,5,5,1]
duplicate(arr)
