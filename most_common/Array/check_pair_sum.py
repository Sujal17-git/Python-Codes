def check_sum(arr):
    sum = int(input("Check Sum Of: "))

    for index_i,value_i in enumerate(arr):
       for index_j,value_j in enumerate(arr[index_i+1::]):
           if value_i + value_j == sum:
               print(f"[{value_i},{value_j}]")
    
arr = [1,2,3,4,5,6,7,8,9,10]
check_sum(arr)

