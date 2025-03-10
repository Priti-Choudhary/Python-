class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_attributes(self):
        print("Name:", self.name)
        print("Age:", self.age)

class MainClass:
    def main(self):
        obj = MyClass("John Doe", 30)
        obj.print_attributes()

# Test
main_obj = MainClass()
main_obj.main()