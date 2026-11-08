arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
current = best = arr[0]
for value in arr[1:]:
    current = max(value, current + value)
    best = max(best, current)
print(best)