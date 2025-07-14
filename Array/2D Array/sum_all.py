# Sum Of All Elements

matrix = [[1,2,3],[4,7,6],[7,8,9]]
sum = 0
for row_index,row in enumerate(matrix):
    
    for colum_index,value in enumerate(row):
       
        sum+=value
        

print(sum)
