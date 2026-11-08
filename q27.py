n = int(input("Enter N: "))
prev = []
for i in range(n):
    row = [1]
    for j in range(1, i):
        row.append(prev[j - 1] + prev[j])
    if i > 0:
        row.append(1)
    print(*row)
    prev = row