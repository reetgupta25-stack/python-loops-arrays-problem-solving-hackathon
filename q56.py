arr = [1, 2, 4, 5, 6]
n = 6
expected = n * (n + 1) // 2
actual = 0
for value in arr:
    actual += value
print(expected - actual)