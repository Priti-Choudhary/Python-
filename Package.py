class ClassA:
    def __init__(self):
        print("Constructor of ClassA")

    def method_a(self):
        print("Method A")

class ClassB:
    def __init__(self):
        print("Constructor of ClassB")

    def method_b(self):
        print("Method B")

from package.ClassA import ClassA
from package.ClassB import ClassB

def main():
    # Create objects
    obj_a = ClassA()
    obj_b = ClassB()

    # Call methods
    obj_a.method_a()
    obj_b.method_b()

if __name__ == "__main__":
    main()
