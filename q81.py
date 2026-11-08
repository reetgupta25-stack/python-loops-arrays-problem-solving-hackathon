matrix = [[1, 2], [3, 4]]
total = 0
for row in matrix:
    for value in row:
        print(value, end=" ")
        total += value
    print()
print("Sum =", total)