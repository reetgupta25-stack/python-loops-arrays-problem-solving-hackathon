matrix = [[1, 2], [3, 4]]
row_sums = []
for row in matrix:
    row_sums.append(sum(row))
col_sums = []
for j in range(len(matrix[0])):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][j]
    col_sums.append(total)
print("Rows =", row_sums)
print("Cols =", col_sums)