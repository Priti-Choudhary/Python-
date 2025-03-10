def handle_exceptions():
    try:
        num1 = 10
        num2 = 0
        result = num1 / num2
    except ZeroDivisionError:
        print("Arithmetic exception occurred")
    finally:
        print("Finally block executed")

handle_exceptions()