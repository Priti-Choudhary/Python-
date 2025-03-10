class PublicClass:
    def __init__(self):
        self.public_field = "Public field"

    def public_method(self):
        return "Public method"

class SamePackageClass:
    def access_public(self):
        obj = PublicClass()
        print(obj.public_field)
        print(obj.public_method())
class DifferentPackageClass:
    def access_public(self):
        obj = PublicClass()
        print(obj.public_field)
        print(obj.public_method())
