def counting_frequency(arr):
    frequency_map ={} #empty dictionary

    for num in arr:
        if num in frequency_map:
            frequency_map[num]+=1
        else:
            frequency_map[num]= 1

    for key in frequency_map:
        print(f"{key} : {frequency_map[key]}")

    return frequency_map

arr = [1,2,1,2,4,2,1,5,5,3]
freq=counting_frequency(arr)

