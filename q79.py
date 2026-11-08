arr = [1, 1, 1]
k = 2
prefix_count = {0: 1}
prefix_sum = 0
count = 0
for value in arr:
    prefix_sum += value
    count += prefix_count.get(prefix_sum - k, 0)
    prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
print(count)