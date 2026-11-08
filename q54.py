arr = [1, 2, 3, 4, 5]
k = 2
if arr:
    k %= len(arr)
    arr = arr[-k:] + arr[:-k] if k else arr[:]
print(arr)