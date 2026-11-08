arr = [4, 2, 7, 1]
x = 7
index = -1
for i in range(len(arr)):
    if arr[i] == x:
        index = i
        break
print(index)