# Global variable  
x = 10  # This is a global variable  

def my_function():  
    # Local variable  
    x = 5  # This is a local variable with the same name as the global variable  

    print("Local x:", x)  # Prints the value of the local variable x  

my_function()  

print("Global x:",x)