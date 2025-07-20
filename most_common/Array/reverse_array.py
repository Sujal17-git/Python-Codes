# Simple
arr = [1,2,3,4,5,6]

print(arr[::-1])

# Trick 2

arr.reverse()
print(arr)

# Trick 3
reverse_arr =[]

for i in range(len(arr)-1,-1,-1):
    reverse_arr.append(arr[i])
print(reverse_arr)

