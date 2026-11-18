matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

print()

rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

mat1 = []
print("Enter matrix 1:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    mat1.append(row)

mat2 = []
print("Enter matrix 2:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    mat2.append(row)

result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(mat1[i][j] + mat2[i][j])
    result.append(row)

print("Sum of matrices:")
for row in result:
    for val in row:
        print(val, end=" ")
    print()
