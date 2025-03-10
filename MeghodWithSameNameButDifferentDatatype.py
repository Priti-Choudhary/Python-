class MyClass:
    def method(self, *args):
        if len(args) == 1 and isinstance(args[0], int):
            print("Method with one integer parameter:", args[0])
        elif len(args) == 1 and isinstance(args[0], str):
            print("Method with one string parameter:", args[0])
        elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], str):
            print("Method with one integer and one string parameter:", args[0], args[1])
        else:
            print("Invalid number or type of parameters")

class MainClass:
    def main(self):
        obj = MyClass()
        obj.method(10)  # Method with one integer parameter
        obj.method("Hello")  # Method with one string parameter
        obj.method(10, "World")  # Method with one integer and one string parameter

# Test
main_obj = MainClass()
main_obj.main()