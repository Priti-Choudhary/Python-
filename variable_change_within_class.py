class MyClass:
    static_var = "I'm a static variable"

MyClass.static_var = "Changed within class"
print(MyClass.static_var)  
obj = MyClass()
print(obj.static_var) 