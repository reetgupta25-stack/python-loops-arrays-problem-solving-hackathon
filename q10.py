digit = 12345
last_digit = 0
first_digit = 0 
for i in range(digit):
    first_digit = digit//10000
    last_digit = digit %10
print(first_digit, last_digit)