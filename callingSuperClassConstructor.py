class SuperClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Superclass default constructor")
        elif arg2 is None:
            print("Superclass one argument constructor:", arg1)
        else:
            print("Superclass two argument constructor:", arg1, arg2)

class ChildClass(SuperClass):
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("ChildClass default constructor")
            super().__init__()
        elif arg2 is None:
            print("ChildClass one argument constructor:", arg1)
            super().__init__(arg1)
        else:
            print("ChildClass two argument constructor:", arg1, arg2)
            super().__init__(arg1, arg2)
class MainClass:
    def main(self):
        # Call default constructor
        obj1 = ChildClass()

        # Call one argument constructor
        obj2 = ChildClass("One argument")

        # Call two argument constructor
        obj3 = ChildClass("Two arguments", "with values")

# Test
main_obj = MainClass()
main_obj.main()
