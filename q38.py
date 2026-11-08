arr = [12,35,1,10,34,1]
largest = arr[0]
secondlarest = arr[0] 
for i in range(len(arr)):
    if arr[i]>largest:
        secondlarest = largest 
        largest = arr[i]
    elif arr[i]>secondlarest:
        secondlarest = arr[i]
print("Largest: ", largest)
print("Second largest: ", secondlarest)
