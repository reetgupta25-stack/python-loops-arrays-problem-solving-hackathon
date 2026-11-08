matrix = [[1, 0], [0, 1]]
n = len(matrix)
is_identity = all(len(row) == n for row in matrix)
if is_identity:
    for i in range(n):
        for j in range(n):
            expected = 1 if i == j else 0
            if matrix[i][j] != expected:
                is_identity = False
                break
        if not is_identity:
            break
print(is_identity)