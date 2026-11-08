matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows, cols = len(matrix), len(matrix[0])
result = []
if rows == 1:
    result.extend(matrix[0])
elif cols == 1:
    result.extend(row[0] for row in matrix)
else:
    result.extend(matrix[0])
    for i in range(1, rows - 1):
        result.append(matrix[i][cols - 1])
    result.extend(reversed(matrix[rows - 1]))
    for i in range(rows - 2, 0, -1):
        result.append(matrix[i][0])
print(result)