def reverse_array(my_list,start=0,end=None):
    if end is None:
        end = len(my_list)-1
    if start>=end:
        return
    my_list[start],my_list[end] =my_list[end],my_list[start]

    reverse_array(my_list, start+1,end-1)



my_list = [1,2,3,4,5]
reverse_array(my_list)

print("Reverse array is:",my_list)