# 3502C Lab 2 Code
# Written by: Michael Muraglia
# 6/5/2023

op1 = float(input("Enter first operand: "))  # Gets first operand from user
op2 = float(input("Enter second operand: "))  # Gets second operand from user

print('Calculator Menu')  # Prints calculator menu and user options
print('---------------')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')

user_selection = int(input('Which operation do you want to perform? '))  # User calculator operation input selection
print()  # Formatting
final_value = 0  # initializing value for final calculated value

if user_selection == 1:  # addition selection
    final_value = op1 + op2
    print('The result of the operation is', final_value, end = '')  # Prints results
    print('. Goodbye!')
elif user_selection == 2: # subtraction selection
    final_value = op1 - op2
    print('The result of the operation is', final_value, end='')  # Prints results
    print('. Goodbye!')
elif user_selection == 3: # division selection
    final_value = op1 * op2
    print('The result of the operation is', final_value, end='')  # Prints results
    print('. Goodbye!')
elif user_selection == 4: # division selection
    final_value = op1 / op2
    print('The result of the operation is', final_value, end='')  # Prints results
    print('. Goodbye!')
else:  # invalid input selection
    print('Error: Invalid selection! Terminating program.')

