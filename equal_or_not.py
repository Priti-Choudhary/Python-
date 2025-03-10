def are_equal(num1, num2):  
  if num1 == num2:  
    return True  
  else:  
    return False  

# Get input from the user (optional)  
number1 = float(input("Enter the first number: "))  
number2 = float(input("Enter the second number: "))  

# Check if the numbers are equal  
if are_equal(number1, number2):  
  print("The numbers are equal.")  
else:  
  print("The numbers are not equal.")