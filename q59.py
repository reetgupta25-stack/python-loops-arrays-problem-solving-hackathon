arr = [1, 2, 3, 4, 5, 6]
even = []
odd = []
for value in arr:
    if value % 2 == 0:
        even.append(value)
    else:
        odd.append(value)
print(even + odd)