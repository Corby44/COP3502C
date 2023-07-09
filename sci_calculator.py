# 3502C Lab 3 Code
# Written by: Michael Muraglia
# 6/13/20233

import math

current_result = float(0.0)  # Initializing current result variable
sum_cal = 0  # Initializing variable for summation of the calculation results
calc_continue = True  # Initializing while loop variable
num_cal = 0  # Initializing variable for number of calculations performed
op1 = 0.0  # Initializing operands for user to enter
op2 = 0.0
RESULT = 0.0  # Result of math operation
no_error = True  # no user entered error


def menu():
    print('\nCalculator Menu')  # Prints calculator menu and user options
    print('---------------')
    print('0. Exit Program')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exponentiation')
    print('6. Logarithm')
    print('7. Display Average')
    local_user_input = int(input('Enter Menu Selection: '))
    return local_user_input


def get_user_input(prev):
    try:  # Previous Took Udacity Python Intro to AI course where I learned try and except for errors
        num_one = float(input('Enter first operand: '))  # asking user for operands
    except ValueError:
        num_one = prev
    try:
        num_two = float(input('Enter second operand: '))
    except ValueError:
        num_two = prev
    return num_one, num_two


print(f'Current Result: {current_result}\n')  # Prints current Results

while calc_continue:
    if no_error:
        user_input = menu()  # Function call for user input (if no user error)
    else:
        user_input = int(input('\nEnter Menu Selection: '))  # Function call for user input (if user error)
        no_error = True
    if user_input == 0:  # user terminates program
        print('\nThanks for using this calculator. Goodbye!')
        break
    elif user_input == 7:  # Prints statistics for calculations
        if num_cal == 0:
            print('Error: No calculations yet to average!')
            no_error = False
        else:
            print(f'\nSum of calculations: {sum_cal}')
            print(f'Number of calculations: {num_cal}')
            average = sum_cal / num_cal  # average calc
            print(f'Average of calculations: {average:.2f}')
            no_error = False  # Technically no error but treats stats as such to get caught in correct gate

    elif user_input == 1:  # addition gate
        op1, op2 = get_user_input(RESULT)
        RESULT = op1 + op2
        print(f'\nCurrent Result: {RESULT}')
        sum_cal += RESULT
        num_cal += 1

    elif user_input == 2:  # Subtraction gate
        op1, op2 = get_user_input(RESULT)
        RESULT = op1 - op2
        print(f'\nCurrent Result: {RESULT}')
        sum_cal += RESULT
        num_cal += 1

    elif user_input == 3:  # Multiplication gate
        op1, op2 = get_user_input(RESULT)
        RESULT = op1 * op2
        print(f'\nCurrent Result: {RESULT}')
        sum_cal += RESULT
        num_cal += 1

    elif user_input == 4:  # Division Gate
        op1, op2 = get_user_input(RESULT)
        RESULT = op1 / op2
        print(f'\nCurrent Result: {RESULT}')
        sum_cal += RESULT
        num_cal += 1

    elif user_input == 5:  # Exponential Gate
        op1, op2 = get_user_input(RESULT)
        RESULT = op1 ** op2
        print(f'\nCurrent Result: {RESULT}')
        sum_cal += RESULT
        num_cal += 1

    elif user_input == 6:  # Log Gate
        op1, op2 = get_user_input(RESULT)
        RESULT = math.log(op2, op1)
        print(f'\nCurrent Result: {RESULT}')
        sum_cal += RESULT
        num_cal += 1
    else:  # Error Gate
        print('Error: Invalid selection!')
        no_error = False
        continue
