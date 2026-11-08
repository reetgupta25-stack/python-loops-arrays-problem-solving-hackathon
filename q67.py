arr = [2, 3, -2, 4]
max_here = min_here = answer = arr[0]
for value in arr[1:]:
    if value < 0:
        max_here, min_here = min_here, max_here
    max_here = max(value, max_here * value)
    min_here = min(value, min_here * value)
    answer = max(answer, max_here)
print(answer)