class MyClass:
    def method(self, *args):
        if len(args) == 1:
            print("Method with one parameter:", args[0])
        elif len(args) == 2:
            print("Method with two parameters:", args[0], args[1])
        else:
            print("Invalid number of parameters")

class MainClass:
    def main(self):
        obj = MyClass()
        obj.method(10)  # Method with one parameter
        obj.method(10, 20)  # Method with two parameters

# Test
main_obj = MainClass()
main_obj.main()