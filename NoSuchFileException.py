def generate_no_such_field_exception():
    class TestClass:
        pass

    obj = TestClass()
    print(obj.non_existent_field)

generate_no_such_field_exception()