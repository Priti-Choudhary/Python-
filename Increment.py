def increment(x):  
  """Increments the value of x by 1."""  
  x += 1  
  return x  

def decrement(x):  
  """Decrements the value of x by 1."""  
  x -= 1  
  return x  

# Example usage:  
number = 5  

number = increment(number)  
print("After increment:", number)  # Output: After increment: 6  

number = decrement(number)  
print("After decrement:",number)