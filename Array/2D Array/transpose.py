matrix = [[1,2,3],[4,7,6],[7,8,9]]

row_len = len(matrix)
col_len = len(matrix[0])

if row_len != col_len:
    print("Matrix is not Symetric")

for row_index,row in enumerate(matrix):
    for col_index,value in enumerate(row):
        if col_index==0:
            print(value,end=" ")