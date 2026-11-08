n = int(input("Enter N: "))
for i in range(n):
    for j in range(n):
        print(1 if (i + j) % 2 == 0 else 0, end=" ")
    print()