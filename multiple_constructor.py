class MyClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default constructor")
        elif arg2 is None:
            print("One argument constructor:", arg1)
        else:
            print("Two argument constructor:", arg1, arg2)

class MainClass:
    def main(self):
        # Call default constructor
        obj1 = MyClass()

        # Call one argument constructor
        obj2 = MyClass("One argument")

        # Call two argument constructor
        obj3 = MyClass("Two arguments", "with values")

# Test
main_obj = MainClass()
main_obj.main()