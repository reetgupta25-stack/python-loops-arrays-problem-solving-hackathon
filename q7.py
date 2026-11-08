n = 1234
sum = 0
while n > 0:
    result = n % 10
    sum+=result
    n = n//10
print(sum)