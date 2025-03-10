age = 30  
print("Integer:", age)  

# Boolean  
is_student = True  
print("Boolean:", is_student)  

# Character (Strings are used for characters in Python)  
initial = 'A'  # Note:  Python doesn't have a separate 'char' type.  We use strings of length 1.  
print("Character:", initial)  

# Float  
price = 99.99  
print("Float:", price)  

# Double (Floats are usually 64-bit, similar to double in other languages)  
pi = 3.141592653589793  
print("Double (Float):", pi)  # Python doesn't have a separate 'double' type, floats are used.  

#Demonstrating that Python floats are usually double-precision (64-bit)  
import sys  
print("Float size in bytes:", sys.getsizeof(price)) #Typically 24 or 28, but the actual float data is 8 bytes.  

# You can also explicitly use the float() constructor to create float variables  
height = float(175)  # Convert an integer to a float  
print("Float from integer:",height)