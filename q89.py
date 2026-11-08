matrix = [[1, 2], [3, 4]]
rotated = []
for j in range(len(matrix[0])):
    new_row = []
    for i in range(len(matrix) - 1, -1, -1):
        new_row.append(matrix[i][j])
    rotated.append(new_row)
print(rotated)