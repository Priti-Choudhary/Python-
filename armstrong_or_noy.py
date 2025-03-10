def is_armstrong(num):
    return num == sum(int(digit) ** len(str(num)) for digit in str(num))

num = 371
if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
