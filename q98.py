matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
saddle = None
for i, row in enumerate(matrix):
    min_value = min(row)
    j = row.index(min_value)
    if all(matrix[r][j] <= min_value for r in range(len(matrix))):
        saddle = min_value
        break
print(saddle if saddle is not None else "No saddle point")