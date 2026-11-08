num = 153 
temp = num
total_sum = 0
while temp > 0:
    digit = temp % 10
    total_sum += digit * digit * digit
    temp //= 10
if total_sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

