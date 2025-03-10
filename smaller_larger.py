def find_smaller_larger(num1, num2):  
  if num1 < num2:  
    smaller = num1  
    larger = num2  
  else:  
    smaller = num2  
    larger = num1  

  return smaller, larger  


# Get input from the user (optional)  
number1 = float(input("Enter the first number: "))  
number2 = float(input("Enter the second number: "))  

# Find the smaller and larger numbers  
smaller, larger = find_smaller_larger(number1, number2)  

# Print the results  
print("Smaller number:", smaller)  
print("Larger number:",larger)