current_operation = input("Which operation would you like to use? (Answer Addition/Subtraction/Multiplication/Division) ")

if current_operation == "Addition":
    number1 = input("What is the first number you would like to add? ")
    number2 = input("What is the second number you would like to add? ")
    addition_answer = int(number1) + int(number2)
    print(f"The sum is {addition_answer}")
elif current_operation == "Subtraction":
    number1 = input("Which number would you like the minuend to be? ")
    number2 = input("Which number would you like the subtrahend to be? ")
    subtraction_answer = int(number1) - int(number2)
    print(f"The difference is {subtraction_answer}")
elif current_operation == "Multiplication":
    number1 = input("What is the first number you would like to multiply? ")
    number2 = input("What is the second number you would like to multiply? ")
    multiplication_answer = int(number1) * int(number2)
    print(f"The product is {multiplication_answer}")
elif current_operation == "Division":
    number1 = input("Which number would you like the dividend to be? ")
    number2 = input("Which number would you like the divisor to be? ")
    division_answer = int(number1) / int(number2)
    print(f"The quotient is {division_answer}")