arr = [1, 2, 2, 3, 1, 4]
frequency = {}
for value in arr:
    frequency[value] = frequency.get(value, 0) + 1
print(frequency)