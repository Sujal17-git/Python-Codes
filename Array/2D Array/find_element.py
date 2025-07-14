rows = int(input("Enter Number of Rows : "))
cols = int(input("Enter Number of Columns : "))

matrix = []

print("Enter Elements Row Wise :")

for i in range(rows):
    row =[]
    for j in range(cols):
        element = int(input(f"Enter Value at index [{i},{j}] : "))
        row.append(element)
    matrix.append(row)

print("The Matrix is :")
for r_index,row in enumerate(matrix):
    for c_index,value in enumerate(row):
        if value == 10:
             print(f"Element at [{r_index},{c_index}] : {value}")
