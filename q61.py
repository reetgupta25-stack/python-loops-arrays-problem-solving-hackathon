arr = [2, 7, 11, 15]
target = 9
seen = {}
answer = None
for i, value in enumerate(arr):
    needed = target - value
    if needed in seen:
        answer = [seen[needed], i]
        break
    seen[value] = i
print(answer if answer is not None else -1)