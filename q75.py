arr = [16, 17, 4, 3, 5, 2]
leaders = []
maximum = float("-inf")
for value in reversed(arr):
    if value > maximum:
        leaders.append(value)
        maximum = value
leaders.reverse()
print(leaders)