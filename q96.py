matrix = [[0, 0, 3], [0, 0, 0], [1, 0, 0]]
total = sum(len(row) for row in matrix)
zero_count = 0
for row in matrix:
    for value in row:
        if value == 0:
            zero_count += 1
print(zero_count > total / 2)