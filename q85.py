matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(matrix)
main_sum = anti_sum = 0
for i in range(n):
    main_sum += matrix[i][i]
    anti_sum += matrix[i][n - 1 - i]
print("Main =", main_sum)
print("Anti =", anti_sum)