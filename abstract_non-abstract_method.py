from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def abstract_method(self):
        pass

    def non_abstract_method(self):
        print("Non-abstract method")