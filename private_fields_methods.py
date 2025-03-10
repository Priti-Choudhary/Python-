class PrivateClass:
    def __init__(self):
        self.__private_field = "Private field"

    def __private_method(self):
        return "Private method"

    def main(self):
        print(self.__private_field)
        print(self.__private_method())

class SubClass(PrivateClass):
    def try_access_private(self):
        try:
            print(self.__private_field)
        except AttributeError:
            print("Cannot access private field")

        try:
            print(self.__private_method())
        except AttributeError:
            print("Cannot access private method")

# Test
obj = PrivateClass()
obj.main()

sub_obj = SubClass()
sub_obj.try_access_private()
