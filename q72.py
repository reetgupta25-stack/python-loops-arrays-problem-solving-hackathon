arr = [2, 1, 5, 1, 3, 2]
k = 3
if k <= 0 or k > len(arr):
    print("Invalid K")
else:
    window_sum = sum(arr[:k])
    best = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        best = max(best, window_sum)
    print(best)