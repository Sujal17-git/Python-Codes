def intersection(arr1,arr2):
    result = []

    for i in arr1:
        if i in arr1 and i in arr2:
            result.append(i)
    return result

first = [1,2,3,4,5]
second = [4,5,6,7,8]

inter = intersection(first,second)

print(inter)

