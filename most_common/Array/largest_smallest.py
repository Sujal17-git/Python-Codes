# Trick 1
arr = [2,4,6,1,3,5]
print(max(arr))
print(min(arr))

#Trick 2
maximum = arr[0]
minimum = arr[0]
for key,value in enumerate(arr):
    if value>maximum:
        maximum=value
    if value<minimum:
        minimum=value
print(f"Minimum From Arr : {minimum}, Maximum from arr {maximum}")    

# 3rd You can sort array and get elements like arr[0] amd arr[-1]