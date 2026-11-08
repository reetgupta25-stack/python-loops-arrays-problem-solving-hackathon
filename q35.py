n = int(input("Enter N: "))
original = n
total = 0
temp = abs(n)
while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    total += fact
    temp //= 10
if original == 0:
    total = 1
print(total == original)