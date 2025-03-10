# Super class A
class A:
    def __init__(self):
        self.a = 10

    def method_a1(self):
        print("Method A1")

    def method_a2(self):
        print("Method A2")

    def override_method(self):
        print("Override method in A")

# Sub class B of A
class B(A):
    def __init__(self):
        super().__init__()
        self.b = 20

    def method_b1(self):
        print("Method B1")

    def method_b2(self):
        print("Method B2")

    def override_method(self):
        print("Override method in B")

# Sub class C of B
class C(B):
    def __init__(self):
        super().__init__()
        self.c = 30

    def method_c1(self):
        print("Method C1")

    def method_c2(self):
        print("Method C2")

    def override_method(self):
        print("Override method in C")

# Main class
class Main:
    @staticmethod
    def main():
        # Create objects
        obj_a = A()
        obj_b = B()
        obj_c = C()

        # Call methods of A
        print("Class A methods:")
        obj_a.method_a1()
        obj_a.method_a2()
        obj_a.override_method()

        # Call methods of B
        print("\nClass B methods:")
        obj_b.method_a1()
        obj_b.method_a2()
        obj_b.method_b1()
        obj_b.method_b2()
        obj_b.override_method()

        # Call methods of C
        print("\nClass C methods:")
        obj_c.method_a1()
        obj_c.method_a2()
        obj_c.method_b1()
        obj_c.method_b2()
        obj_c.method_c1()
        obj_c.method_c2()
        obj_c.override_method()

        # Runtime polymorphism
        print("\nRuntime polymorphism:")
        A.override_method(obj_b)
        A.override_method(obj_c)

        # Accessing data members
        print("\nData members:")
        print(obj_a.a)
        print(obj_b.a)
        print(obj_b.b)
        print(obj_c.a)
        print(obj_c.b)
        print(obj_c.c)

if __name__ == "__main__":
    Main.main()
