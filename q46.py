arr = [1, 2, 2, 3, 4, 4]
unique = []
for value in arr:
    if arr.count(value) == 1:
        unique.append(value)
print(unique)