class MyClass:
    static_var = "I'm a static variable"

obj = MyClass()
obj.static_var = "Changed within instance"
print(MyClass.static_var)
print(obj.static_var)