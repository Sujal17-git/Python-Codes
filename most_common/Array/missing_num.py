arr = [1, 2, 3, 4, 5, 7, 8, 9]

for i in range(len(arr) - 1):
    if arr[i + 1] != arr[i] + 1:
        for missing in range(arr[i] + 1, arr[i + 1]):
            print(f"{missing} is Missing")

