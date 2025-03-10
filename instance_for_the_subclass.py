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

    def call_abstract_method(self):
        obj = ChildClass()
        obj.abstract_method()

    def test_abstract_method(self):
        # We can also call abstract method directly
        self.abstract_method()

# Test
child_obj = ChildClass()
child_obj.call_abstract_method()
child_obj.test_abstract_method()
child_obj.non_abstract_method()

