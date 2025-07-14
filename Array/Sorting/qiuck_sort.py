def quick_sort(arr, low, high):
    # Base case: if one or no elements, already sorted
    if low < high:
        # Partition the array and get pivot's final position
        pi = partition(arr, low, high)
        # Recursively sort left subarray (elements < pivot)
        quick_sort(arr, low, pi - 1)
        # Recursively sort right subarray (elements > pivot)
        quick_sort(arr, pi + 1, high)
    return arr

def partition(arr, low, high):
    # Choose last element as pivot
    pivot = arr[high]
    # i tracks position for elements <= pivot
    i = low - 1
    # Compare each element with pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1  # Move boundary of smaller elements
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    # Place pivot in its final position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # Return pivot's position
    return i + 1

# Test with your array
arr = [4, 3, 5, 1, 2]
n = len(arr)
sorted_arr = quick_sort(arr, 0, n - 1)
print(f"Sorted array: {sorted_arr}")