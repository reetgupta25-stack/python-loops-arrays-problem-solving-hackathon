n = int(input("Enter N: "))
if n <= 0:
    raise ValueError("N must be positive")
while n != 1:
    print(n, end=" ")
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
print(1)