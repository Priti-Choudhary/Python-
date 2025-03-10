def handle_exceptions():
    try:
        num1 = 10
        num2 = 0
        result = num1 / num2
    except ZeroDivisionError:
        print("Arithmetic exception occurred")
    except TypeError:
        print("Type exception occurred")
    except Exception as e:
        print("General exception occurred: ", str(e))

handle_exceptions()
