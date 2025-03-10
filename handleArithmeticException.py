def handle_arithmetic_exception():
    try:
        num1 = 10
        num2 = 0
        result = num1 / num2
    except ZeroDivisionError:
        print("Arithmetic exception occurred: Cannot divide by zero!")

handle_arithmetic_exception()