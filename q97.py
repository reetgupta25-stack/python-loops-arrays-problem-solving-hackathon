matrix = [[1, 2], [3, 4]]
rows, cols = len(matrix), len(matrix[0])
result = []
for s in range(rows + cols - 1):
    diagonal = []
    for i in range(rows):
        j = s - i
        if 0 <= j < cols:
            diagonal.append(matrix[i][j])
    result.append(diagonal)
print(result)