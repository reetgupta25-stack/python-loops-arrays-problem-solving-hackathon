arr = [1, 3, 5, 7, 9]
target = 7
left, right = 0, len(arr) - 1
index = -1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        index = mid
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
print(index)