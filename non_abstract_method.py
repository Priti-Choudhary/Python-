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

    def call_non_abstract_method(self):
        obj = ChildClass()
        obj.non_abstract_method()

    def test_non_abstract_method(self):
        # We can also call non-abstract method directly
        self.non_abstract_method()

# Test
child_obj = ChildClass()
child_obj.call_non_abstract_method()
child_obj.test_non_abstract_method()
child_obj.abstract_method()

