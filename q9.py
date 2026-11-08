num = int(input("Write an input: "))
reverse = 0
original_num = num
while num>0:
    digit = num %10
    reverse = reverse*10 + digit
    num = num //10

if reverse == original_num:
    print("its palindrome")
else:
    print("Its not plindrome")