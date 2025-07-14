def devide_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid = len(arr)//2

        left_half = arr[:mid]
        right_half = arr[mid:]
        left_half = devide_sort(left_half)
        right_half = devide_sort(right_half)

        return merge_sort(left_half,right_half)

def merge_sort(left,right):
    new=[]
    i,j=0,0

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

arr = [4,3,5,1,2]

sorted_arr= devide_sort(arr)

print(f"Sorted array {sorted_arr}")