from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def abstract_method(self):
        pass

    def non_abstract_method(self):
        print("Non-abstract method")

class ChildClass(AbstractClass):
    def __init__(self):
        super().__init__()

    def abstract_method(self):
        print("Abstract method implemented in ChildClass")

    def access_non_abstract_method(self):
        # Create an object of AbstractClass is not possible
        # Because AbstractClass is an abstract class
        # Instead, we can create an object of ChildClass
        obj = ChildClass()
        obj.non_abstract_method()

    def test_non_abstract_method(self):
        # We can also access non-abstract method directly
        self.non_abstract_method()
child_obj = ChildClass()
child_obj.access_non_abstract_method()
child_obj.test_non_abstract_method()
child_obj.abstract_method()

