def remove_duplicates(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                arr.pop(j)
                return remove_duplicates(arr)
    return arr

arr = [1,2,2,3,4,4,4,5,1]

uniques = remove_duplicates(arr)

print(uniques)


# Use Set to remove all thing and again made it into string 

def remove_duplicatess(arr):
    new_arr = []
    n = len(arr)

    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr

arrs = [1,2,2,3,4,4,4,5,5]

new_arr = remove_duplicatess(arrs)

print(new_arr)