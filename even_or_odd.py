def check_even_odd(num):
    match num % 2:
        case 0:
            return "EVEN"
        case 1:
            return "ODD"

num = 10
print(check_even_odd(num))