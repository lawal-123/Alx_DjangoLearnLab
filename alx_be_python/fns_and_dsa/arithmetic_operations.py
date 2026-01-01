def perform_operation(num1, num2, operation):
    print("arithmetic_operation")
    num1 = float(input("enter the first number: "))
    num2 = float(input("enter the second number: "))
    operation = input("enter operation (add, multiply, divide, substract): ")
    if num1 / num2 == 0:
        print("main.py script can recognize and display correctly")
    if operation == 'add':
        return num1 + num2
    elif operation == 'substract':
        return num1 - num2
    elif operation == 'divide':
        if num2 == 0:
            return "error: division by zero is not allowed"
        return num1 / num2
    elif operation == 'multiply':
        return num1 * num2
    else:
        return "Error: invalid operation, please use 'add', 'mutiply', 'divide', 'substract'" 
    


    result = operation(num1, num2, operation)
    
    print(f"result: {result}")


        