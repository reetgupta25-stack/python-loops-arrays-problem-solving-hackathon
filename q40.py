arr = [-1,2, 0, -3, 5, 0]
positive_count = 0
negative_count = 0 
zero_count = 0 
for i in range(len(arr)):
    if arr[i]>0:
        positive_count+=1
    elif arr[i]<0:
        negative_count+=1
    else:
        zero_count+=1
print("Negative Count: ", negative_count, "Positive Count: ", positive_count, "Zero Count: ", zero_count)