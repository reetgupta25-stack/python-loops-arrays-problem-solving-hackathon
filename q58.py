arr = [3, 2, 3]
candidate = None
count = 0
for value in arr:
    if count == 0:
        candidate = value
    count += 1 if value == candidate else -1
if arr.count(candidate) > len(arr) // 2:
    print(candidate)
else:
    print("No majority element")