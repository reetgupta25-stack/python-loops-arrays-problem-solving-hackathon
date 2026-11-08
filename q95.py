matrix = [[0, 1, 1], [1, 1, 1], [0, 0, 1]]
best_row = -1
max_ones = -1
for i, row in enumerate(matrix):
    count = sum(row)
    if count > max_ones:
        max_ones = count
        best_row = i
print("Row", best_row)