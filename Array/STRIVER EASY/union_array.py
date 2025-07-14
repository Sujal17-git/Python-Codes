def union_of_arr(arr1,arr2):
    
    union =[]

    for i in arr1:
        if i not in union:
            union.append(i)
        
    for j in arr2:
        if j not in union:
            union.append(j)
    
    return union

first = [1,2,3,4,5]
second = [4,5,6,7,8]

union_result = union_of_arr(first,second)

print(union_result)