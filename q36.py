arr = [1,2,3,4,5]
sum = 0
avg = 0 
for i in range(len(arr)):
    sum += arr[i]
    avg = sum/len(arr)
print(sum)
print(avg)