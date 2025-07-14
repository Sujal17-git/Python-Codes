def devide_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid = len(arr)//2
        left_arr=arr[:mid]
        right_arr=arr[mid:]
        left_arr = devide_sort(left_arr)
        right_arr = devide_sort(right_arr)

        return merge_sort(left_arr,right_arr)


def merge_sort(left,right):
    new = []
    i,j = 0,0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1

    new.extend(left[i:])
    new.extend(right[j:])

    return new

arraay = [3,2,5,1,6]

sor = devide_sort(arraay)

print(f"{sor}")

        