n = int(input("Enter decimal number: "))
binary = ""
if n == 0:
    binary = "0"
while n > 0:
    remainder = n % 2
    binary += str(remainder)
    n = n // 2
binary = binary[::-1]
print(binary)