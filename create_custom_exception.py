class CustomException(Exception):
    pass

def throw_custom_exception():
    raise CustomException("Custom exception occurred")

try:
    throw_custom_exception()
except CustomException as e:
    print(str(e))