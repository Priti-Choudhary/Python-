class MyClass:
    def __init__(self):
        pass

    def __private_constructor(self):
        print("Private constructor")

    def _protected_constructor(self):
        print("Protected constructor")

    def public_constructor(self):
        print("Public constructor")

class MainClass:
    def main(self):
        obj = MyClass()
        # obj.__private_constructor()  # This will raise an error
        obj._MyClass__private_constructor()  # Name mangling
        obj._protected_constructor()
        obj.public_constructor()

# Test
main_obj = MainClass()
main_obj.main()