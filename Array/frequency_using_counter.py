from collections import Counter

def counting_frequenct(arr):
    freq_map  = Counter(arr)
    for key in freq_map:
        print(f"{key} : {freq_map[key]}")

    if freq_map:
        min_freq = min(freq_map.values())
        max_freq = max(freq_map.values())

        min_key = [key for key,value in freq_map.items() if value == min_freq]
        max_key = [key for key,value in freq_map.items() if value == max_freq]

        print(f"Maximun Frequency {max_freq} Elements{max_key}")
        print(f"Mininum Frequency {min_freq} Elements{min_key}")

    return dict(freq_map)

arr = [1,2,1,2,4,2,1,5,5,3,6]
freq=counting_frequenct(arr)