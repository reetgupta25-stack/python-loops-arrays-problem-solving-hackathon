arr = [1, 1, 2, 2, 3]
if arr:
    write = 1
    for read in range(1, len(arr)):
        if arr[read] != arr[write - 1]:
            arr[write] = arr[read]
            write += 1
    del arr[write:]
print("Length =", len(arr))
print("arr =", arr)