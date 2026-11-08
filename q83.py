A = [[1, 2], [3, 4]]
B = [[1, 0], [0, 1]]
rows_a, cols_a = len(A), len(A[0])
rows_b, cols_b = len(B), len(B[0])
if cols_a != rows_b:
    print("Multiplication not possible")
else:
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += A[i][k] * B[k][j]
    print(result)