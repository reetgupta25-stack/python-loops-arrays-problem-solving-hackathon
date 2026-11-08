matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
target = 5
i, j = 0, len(matrix[0]) - 1
position = None
while i < len(matrix) and j >= 0:
    if matrix[i][j] == target:
        position = (i, j)
        break
    elif matrix[i][j] > target:
        j -= 1
    else:
        i += 1
print(position if position is not None else "Not found")