arr1 = [1,2,3,4,5]
arr2 = [4,5,6,7,8]

for index,value in enumerate(arr2):
    if value not in arr1:
        arr1.append(value)
print(arr1)

arr3 = [1,2,3,4,5]
arr4 = [4,5,6,7,8]

result =[]

for ind,val in enumerate(arr3):
    if val in arr4:
        result.append(val)
print(result)