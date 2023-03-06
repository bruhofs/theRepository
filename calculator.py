while True:
    print("Enter 'x' to exit.")
    num1 = input("Enter first number: ")
    if num1 == 'x':
        break
    num2 = input("Enter second number: ")
    if num2 == 'x':
        break

    # convert inputs to float values
    num1 = float(num1)
    num2 = float(num2)

    operation = input("Enter operation (+, -, /,*): ")
    if operation == 'x':
        break

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '/':
        if num2 == 0:
            print("Error: division by zero")
            continue
        result = num1 / num2
    elif operation == '*':
        result = num1 * num2
    else:
        print("Invalid input")
        continue

    # format result to display 2 decimal places without trailing zeros
    num1format = "{:.10f}".format(num1).rstrip('0').rstrip('.')
    num2format = "{:.10f}".format(num2).rstrip('0').rstrip('.')
    result_str = "{:.2f}".format(result).rstrip('0').rstrip('.')
    print(num1format, operation, num2format, "=", result_str)