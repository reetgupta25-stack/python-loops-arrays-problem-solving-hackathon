arr = [-7, 1, 5, 2, -4, 3, 0]
total = sum(arr)
left_sum = 0
answer = -1
for i, value in enumerate(arr):
    total -= value
    if left_sum == total:
        answer = i
        break
    left_sum += value
print(answer)