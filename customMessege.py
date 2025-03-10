def throw_custom_exception():
    try:
        num1 = 10
        num2 = 0
        result = num1 / num2
    except ZeroDivisionError:
        raise Exception("Custom arithmetic exception occurred")

try:
    throw_custom_exception()
except Exception as e:
    print(str(e))