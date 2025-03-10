class ProtectedClass:
    def __init__(self):
        self._protected_field = "Protected field"

    def _protected_method(self):
        return "Protected method"

class SamePackageClass:
    def access_protected(self):
        obj = ProtectedClass()
        print(obj._protected_field)
        print(obj._protected_method())

class DifferentPackageClass:
    def access_protected(self):
        obj = ProtectedClass()
        print(obj._protected_field)
        print(obj._protected_method())

class ChildClass(ProtectedClass):
    def access_protected(self):
        print(self._protected_field)
        print(self._protected_method())