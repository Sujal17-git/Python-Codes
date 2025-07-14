# Sum Of All Elements

matrix = [[1,2,3],[4,7,6],[7,8,9]]
sum0 = 0
sum1 = 0
sum2 = 0
for row_index,row in enumerate(matrix):
    for colum_index,value in enumerate(row):
       
        if colum_index == 0:
            sum0+=value
        elif colum_index == 1:
            sum1+=value
        elif colum_index == 2:
            sum2+=value
print("Sum when column is 0 :",sum0)
print("Sum when column is 1 :",sum1)
print("Sum when column is 2 :",sum2)