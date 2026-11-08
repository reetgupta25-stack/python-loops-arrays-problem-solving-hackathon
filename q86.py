matrix = [[1, 2], [2, 1]]
n = len(matrix)
symmetric = all(len(row) == n for row in matrix)
if symmetric:
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                symmetric = False
                break
        if not symmetric:
            break
print(symmetric)