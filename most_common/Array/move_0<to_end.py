arr1 =[1,2,0,2,1,0,8,0]

for index,value in enumerate(arr1):
    if value == 0:
        arr1.pop(index)
        arr1.append(0)
print(arr1)

# Another and best approach

arr = [1, 2, 0, 2, 1, 0, 8, 0]

non_zero_pos = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[non_zero_pos] = arr[i]
        non_zero_pos += 1

for i in range(non_zero_pos, len(arr)):
    arr[i] = 0

print("Array after moving all zeros to the end:")
print(arr)
