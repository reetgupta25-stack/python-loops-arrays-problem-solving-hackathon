arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
from collections import deque
if k <= 0 or k > len(arr):
    print([])
else:
    negatives = deque()
    result = []
    for i, value in enumerate(arr):
        if value < 0:
            negatives.append(i)
        while negatives and negatives[0] <= i - k:
            negatives.popleft()
        if i >= k - 1:
            result.append(arr[negatives[0]] if negatives else 0)
    print(result)