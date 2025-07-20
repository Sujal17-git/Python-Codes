arr =[1,4,2,7,5,6]

arr.sort()
arr.reverse()

n = int(input("enter k :"))
if n>len(arr):
    print("Array out of bound")
elif 0>=n:
    print("Plese enter valid K")
else:
    print(arr[n-1])