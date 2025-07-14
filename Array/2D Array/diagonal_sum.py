matrix = [[10,2,3],[4,20,6],[7,8,30]]
sum = 0
for row_index,row in enumerate(matrix):
    for col_index,value in enumerate(row):
        if row_index==col_index:
            sum+=value

print(f"Sum of diagonal matrix is {sum}")
