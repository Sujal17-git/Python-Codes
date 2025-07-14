def left_rotate(arr):
   n =3
   for i in range(3):
        temp = arr[0]
        arr.pop(0)
        arr.append(temp)

   return arr

arr = [1,2,3,4,5]
left = left_rotate(arr)
print(left)