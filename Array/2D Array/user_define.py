rows = int(input("Enter Total Number Of Rows : "))
colum = int(input("Enter Total Numbers of Columns :"))

matrix = []
print("Enter Matrix Element Row wise")

for i in range(rows):
    row =[]
    for j in range(colum):
        elements = int(input(f"Enter Element at [{i},{j}]"))
        row.append(elements)
    matrix.append(row)

print("\n Matrix Is :")
for row in matrix:
    print(row)

    