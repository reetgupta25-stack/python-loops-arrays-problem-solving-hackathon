arr = [4,9,1,7,3]
max = arr[0]
min = arr[0]
for i in range(len(arr)):
    if max<arr[i]:
        max = arr[i]
    if min>arr[i]:
        min = arr[i]
print(max)
print(min)