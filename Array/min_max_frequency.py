def counting_frequency(arr):
    frequency_map = {} # empty dictionary

    for num in arr:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1

    for key in frequency_map:
        print(f"{key} : {frequency_map[key]}")

    # Find min and max frequencies
    if frequency_map:  # Ensure dictionary is not empty
        min_freq = min(frequency_map.values())
        max_freq = max(frequency_map.values())

        # Find all keys with min and max frequencies
        min_elements = [key for key, value in frequency_map.items() if value == min_freq]
        max_elements = [key for key, value in frequency_map.items() if value == max_freq]

        # Print min and max elements
        print(f"Element(s) with minimum frequency ({min_freq}): {min_elements}")
        print(f"Element(s) with maximum frequency ({max_freq}): {max_elements}")

    return frequency_map

arr = [1, 2, 1, 2, 4, 2, 1, 5, 5, 3]
freq = counting_frequency(arr)