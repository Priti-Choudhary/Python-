def arithmetic_operations(num1, num2, operator):  
    if operator == '+':  
        return num1 + num2  
    elif operator == '-':  
        return num1 - num2  
    elif operator == '*':  
        return num1 * num2  
    elif operator == '/':  
        if num2 == 0:  
            print("Error: Division by zero is not allowed.")  
            return None  
        return num1 / num2  
    else:  
        print("Error: Invalid operator. Please use +, -, *, or /.")  
        return None  
