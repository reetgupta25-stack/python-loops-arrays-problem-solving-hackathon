arr = [1, 2, 2, 4, 5]
is_sorted = True
for i in range(1, len(arr)):
    if arr[i] < arr[i - 1]:
        is_sorted = False
        break
print(is_sorted)