arr = [0, 1, 0, 3, 12]
write = 0
for value in arr:
    if value != 0:
        arr[write] = value
        write += 1
while write < len(arr):
    arr[write] = 0
    write += 1
print(arr)