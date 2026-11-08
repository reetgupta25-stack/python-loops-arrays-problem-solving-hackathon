n = int(input("Enter N: "))
if n <= 0:
    print("Invalid N")
elif n == 1:
    print(0)
else:
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    print(b)